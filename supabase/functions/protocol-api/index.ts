import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "jsr:@supabase/supabase-js@2";

const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_ROLE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders, "Content-Type": "application/json" },
  });
}

// --- Calendário lunar: aproximação padrão de lua nova (referência 2000-01-06 18:14 UTC) ---
const SYNODIC_MONTH_DAYS = 29.530588853;
const KNOWN_NEW_MOON_MS = Date.UTC(2000, 0, 6, 18, 14, 0);

function nextNewMoon(fromDate: Date): Date {
  const fromMs = fromDate.getTime();
  const daysSinceKnown = (fromMs - KNOWN_NEW_MOON_MS) / 86400000;
  let n = Math.floor(daysSinceKnown / SYNODIC_MONTH_DAYS);
  let candidate = new Date(KNOWN_NEW_MOON_MS + n * SYNODIC_MONTH_DAYS * 86400000);
  while (candidate.getTime() < fromMs) {
    n += 1;
    candidate = new Date(KNOWN_NEW_MOON_MS + n * SYNODIC_MONTH_DAYS * 86400000);
  }
  return candidate;
}

function toDateOnly(d: Date): string {
  return d.toISOString().slice(0, 10);
}

function addDays(dateStr: string, days: number): string {
  const d = new Date(dateStr + "T00:00:00Z");
  d.setUTCDate(d.getUTCDate() + days);
  return toDateOnly(d);
}

// --- Cronograma dos protocolos (ver CLAUDE.md, seção 5) ---
type ChecklistItem = {
  key: string;
  label: string;
  instrucao: string;
  offsetStart: number;
  offsetEnd: number;
  vezesPorDia: number;
};

const ADULT_ITEMS: ChecklistItem[] = [
  { key: "silimarina", label: "Silimarina 200mg", instrucao: "1 cápsula após o café da manhã + 1 cápsula após o jantar", offsetStart: -15, offsetEnd: -1, vezesPorDia: 2 },
  { key: "tintura", label: "Tintura (fórmula fitoterápica)", instrucao: "3ml diluídos em água, antes das refeições", offsetStart: 0, offsetEnd: 14, vezesPorDia: 3 },
  { key: "oleo_oregano", label: "Óleo de Orégano", instrucao: "1 cápsula antes das refeições, junto com a tintura", offsetStart: 0, offsetEnd: 14, vezesPorDia: 3 },
  { key: "ornitina", label: "Ornitina 550mg", instrucao: "1 cápsula, 30 minutos antes de deitar", offsetStart: 0, offsetEnd: 14, vezesPorDia: 1 },
];

const KIDS_ITEMS: ChecklistItem[] = [
  { key: "fitoterapia_kids", label: "Fitoterapia potencializadora", instrucao: "15–20 min antes da tintura (ou junto, se for mais fácil pra criança)", offsetStart: 0, offsetEnd: 29, vezesPorDia: 3 },
  { key: "tintura_kids", label: "Tintura de desparasitação", instrucao: "Diluir em 50ml de água", offsetStart: 0, offsetEnd: 29, vezesPorDia: 3 },
];

function itemsFor(tipo: string): ChecklistItem[] {
  return tipo === "kids" ? KIDS_ITEMS : ADULT_ITEMS;
}

function buildRunDates(tipo: string, moonDateStr: string) {
  const items = itemsFor(tipo);
  const minOffset = Math.min(...items.map((i) => i.offsetStart));
  const maxOffset = Math.max(...items.map((i) => i.offsetEnd));
  return {
    moon_date: moonDateStr,
    silimarina_start_date: tipo === "adulto" ? addDays(moonDateStr, minOffset) : null,
    start_date: moonDateStr,
    end_date: addDays(moonDateStr, maxOffset),
    phase_start_date: addDays(moonDateStr, minOffset),
  };
}

// --- Parsing dos dados reais de compra (tabela compra_aprovada) ---
function detectarProdutos(produtoStr: string): { adulto: number; kids_2_4: number; kids_5_9: number; familia: number; oleo_alho: number } {
  const s = produtoStr || "";
  const count = (re: RegExp) => {
    const m = s.match(re);
    if (!m) return 0;
    const qtyMatch = s.slice(m.index).match(/\(x(\d+)\)/);
    return qtyMatch ? parseInt(qtyMatch[1], 10) : 1;
  };
  return {
    adulto: count(/VermeFree Adulto/i),
    kids_2_4: count(/Kids 2 a 4/i),
    kids_5_9: count(/Kids 5 a 9/i),
    familia: count(/Kit Desparasitação Família/i),
    oleo_alho: count(/[oó]leo de alho/i),
  };
}

function parseQuizCheckout(quizStr: string | null): Record<string, string> | null {
  if (!quizStr) return null;
  const out: Record<string, string> = {};
  const linhas = quizStr.split("\n");
  for (const linha of linhas) {
    const m = linha.match(/^([^:]+):\s*(.+)$/);
    if (m) out[m[1].trim()] = m[2].trim();
  }
  return out;
}

async function getCustomerByToken(supabase: ReturnType<typeof createClient>, accessToken: string) {
  const { data, error } = await supabase
    .from("app_customers")
    .select("*")
    .eq("access_token", accessToken)
    .maybeSingle();
  if (error) throw error;
  return data;
}

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: corsHeaders });
  if (req.method !== "POST") return json({ error: "method_not_allowed" }, 405);

  const supabase = createClient(SUPABASE_URL, SERVICE_ROLE_KEY);

  let body: Record<string, unknown>;
  try {
    body = await req.json();
  } catch {
    return json({ error: "invalid_json" }, 400);
  }

  const action = body.action as string;

  try {
    if (action === "verify-purchase") {
      const email = String(body.email || "").trim().toLowerCase();
      const idCompra = Number(body.id_compra);
      if (!email || !idCompra) return json({ error: "missing_fields" }, 400);

      const { data: compra, error: compraErr } = await supabase
        .from("compra_aprovada")
        .select("id_compra, email, nome, produto, quiz")
        .eq("id_compra", idCompra)
        .ilike("email", email)
        .maybeSingle();
      if (compraErr) throw compraErr;
      if (!compra) return json({ error: "not_found" }, 404);

      const produtos = detectarProdutos(compra.produto as string);
      const quizCheckout = parseQuizCheckout(compra.quiz as string | null);

      const { data: customer, error: upsertErr } = await supabase
        .from("app_customers")
        .upsert(
          {
            email,
            nome: compra.nome,
            id_compra: compra.id_compra,
            produtos,
            quiz_checkout: quizCheckout,
          },
          { onConflict: "email" },
        )
        .select("*")
        .single();
      if (upsertErr) throw upsertErr;

      return json({
        access_token: customer.access_token,
        customer: { id: customer.id, nome: customer.nome, email: customer.email },
        produtos,
        quiz_checkout: quizCheckout,
      });
    }

    if (action === "get-state") {
      const accessToken = String(body.access_token || "");
      const customer = await getCustomerByToken(supabase, accessToken);
      if (!customer) return json({ error: "invalid_token" }, 401);

      const { data: profiles, error: profErr } = await supabase
        .from("app_profiles")
        .select("*")
        .eq("customer_id", customer.id)
        .order("created_at", { ascending: true });
      if (profErr) throw profErr;

      const profileIds = (profiles || []).map((p) => p.id);
      const { data: runs, error: runsErr } = profileIds.length
        ? await supabase
            .from("app_protocol_runs")
            .select("*")
            .in("profile_id", profileIds)
            .order("created_at", { ascending: false })
        : { data: [], error: null };
      if (runsErr) throw runsErr;

      const runIds = (runs || []).map((r) => r.id);
      const { data: checks, error: checksErr } = runIds.length
        ? await supabase.from("app_daily_checks").select("*").in("run_id", runIds)
        : { data: [], error: null };
      if (checksErr) throw checksErr;

      return json({
        customer: { id: customer.id, nome: customer.nome, email: customer.email, produtos: customer.produtos, quiz_checkout: customer.quiz_checkout },
        profiles: profiles || [],
        runs: runs || [],
        checks: checks || [],
        items_adulto: ADULT_ITEMS,
        items_kids: KIDS_ITEMS,
      });
    }

    if (action === "save-profiles") {
      const accessToken = String(body.access_token || "");
      const customer = await getCustomerByToken(supabase, accessToken);
      if (!customer) return json({ error: "invalid_token" }, 401);

      const perfis = (body.profiles as Array<{ tipo: string; nome: string; faixa_etaria?: string }>) || [];
      if (!perfis.length) return json({ error: "no_profiles" }, 400);

      const hoje = new Date();
      const moonDateStr = body.moon_date ? String(body.moon_date) : toDateOnly(nextNewMoon(hoje));

      const created = [];
      for (const perfil of perfis) {
        const { data: profile, error: profErr } = await supabase
          .from("app_profiles")
          .insert({ customer_id: customer.id, tipo: perfil.tipo, nome: perfil.nome, faixa_etaria: perfil.faixa_etaria || null })
          .select("*")
          .single();
        if (profErr) throw profErr;

        const dates = buildRunDates(perfil.tipo, moonDateStr);
        const todayStr = toDateOnly(hoje);
        const status = todayStr >= dates.phase_start_date ? "em_andamento" : "agendado";

        const { data: run, error: runErr } = await supabase
          .from("app_protocol_runs")
          .insert({
            profile_id: profile.id,
            moon_date: dates.moon_date,
            silimarina_start_date: dates.silimarina_start_date,
            start_date: dates.start_date,
            end_date: dates.end_date,
            status,
          })
          .select("*")
          .single();
        if (runErr) throw runErr;

        created.push({ profile, run });
      }

      return json({ created });
    }

    if (action === "toggle-check") {
      const accessToken = String(body.access_token || "");
      const customer = await getCustomerByToken(supabase, accessToken);
      if (!customer) return json({ error: "invalid_token" }, 401);

      const runId = String(body.run_id || "");
      const checkDate = String(body.check_date || "");
      const itemKey = String(body.item_key || "");
      const done = Boolean(body.done);

      const { data: run, error: runErr } = await supabase
        .from("app_protocol_runs")
        .select("id, profile_id, app_profiles!inner(customer_id)")
        .eq("id", runId)
        .maybeSingle();
      if (runErr) throw runErr;
      if (!run || (run as unknown as { app_profiles: { customer_id: string } }).app_profiles.customer_id !== customer.id) {
        return json({ error: "forbidden" }, 403);
      }

      const { error: upsertErr } = await supabase
        .from("app_daily_checks")
        .upsert(
          { run_id: runId, check_date: checkDate, item_key: itemKey, done, done_at: done ? new Date().toISOString() : null },
          { onConflict: "run_id,check_date,item_key" },
        );
      if (upsertErr) throw upsertErr;

      return json({ ok: true });
    }

    if (action === "complete-run") {
      const accessToken = String(body.access_token || "");
      const customer = await getCustomerByToken(supabase, accessToken);
      if (!customer) return json({ error: "invalid_token" }, 401);

      const runId = String(body.run_id || "");
      const transformacao = String(body.transformacao || "");
      const relato = body.relato ? String(body.relato) : null;

      const { data: run, error: runErr } = await supabase
        .from("app_protocol_runs")
        .select("id, app_profiles!inner(customer_id)")
        .eq("id", runId)
        .maybeSingle();
      if (runErr) throw runErr;
      if (!run || (run as unknown as { app_profiles: { customer_id: string } }).app_profiles.customer_id !== customer.id) {
        return json({ error: "forbidden" }, 403);
      }

      const precisaReforco = transformacao === "leve" || transformacao === "nenhuma";
      const recomendacao = precisaReforco ? "repetir_proximo_ciclo" : "manutencao_normal";
      const cupomOferecido = precisaReforco ? "5OFF" : null;

      const { error: quizErr } = await supabase.from("app_quiz_responses").insert({
        run_id: runId,
        transformacao,
        relato,
        recomendacao,
        cupom_oferecido: cupomOferecido,
      });
      if (quizErr) throw quizErr;

      const { error: updateErr } = await supabase
        .from("app_protocol_runs")
        .update({ status: "concluido", completed_at: new Date().toISOString() })
        .eq("id", runId);
      if (updateErr) throw updateErr;

      return json({ recomendacao, cupom_oferecido: cupomOferecido });
    }

    return json({ error: "unknown_action" }, 400);
  } catch (err) {
    console.error(err);
    return json({ error: "internal_error", detail: String(err) }, 500);
  }
});
