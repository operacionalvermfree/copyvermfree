export type TipoPerfil = 'adulto' | 'kids';

export type ProdutosComprados = {
  adulto: number;
  kids_2_4: number;
  kids_5_9: number;
  familia: number;
  oleo_alho: number;
};

export type QuizCheckout = Record<string, string>;

export type Customer = {
  id: string;
  nome: string | null;
  email: string;
  produtos?: ProdutosComprados;
  quiz_checkout?: QuizCheckout | null;
};

export type Profile = {
  id: string;
  customer_id: string;
  tipo: TipoPerfil;
  nome: string;
  faixa_etaria: string | null;
  created_at: string;
};

export type RunStatus = 'agendado' | 'em_andamento' | 'concluido' | 'abandonado';

export type ProtocolRun = {
  id: string;
  profile_id: string;
  moon_date: string;
  silimarina_start_date: string | null;
  start_date: string;
  end_date: string;
  status: RunStatus;
  created_at: string;
  completed_at: string | null;
};

export type DailyCheck = {
  id: string;
  run_id: string;
  check_date: string;
  item_key: string;
  done: boolean;
  done_at: string | null;
};

export type ChecklistItem = {
  key: string;
  label: string;
  instrucao: string;
  offsetStart: number;
  offsetEnd: number;
  vezesPorDia: number;
};

export type AppState = {
  customer: Customer;
  profiles: Profile[];
  runs: ProtocolRun[];
  checks: DailyCheck[];
  items_adulto: ChecklistItem[];
  items_kids: ChecklistItem[];
};

export type ProfileInput = {
  tipo: TipoPerfil;
  nome: string;
  faixa_etaria?: string;
};

export type Transformacao = 'bastante' | 'leve' | 'nenhuma';

export type CompleteRunResult = {
  recomendacao: 'repetir_proximo_ciclo' | 'manutencao_normal';
  cupom_oferecido: string | null;
};
