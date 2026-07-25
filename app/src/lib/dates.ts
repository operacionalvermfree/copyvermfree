import type { ChecklistItem, ProtocolRun } from './types';

export function todayStr(): string {
  return new Date().toISOString().slice(0, 10);
}

export function addDays(dateStr: string, days: number): string {
  const d = new Date(dateStr + 'T00:00:00Z');
  d.setUTCDate(d.getUTCDate() + days);
  return d.toISOString().slice(0, 10);
}

export function daysBetween(fromStr: string, toStr: string): number {
  const a = new Date(fromStr + 'T00:00:00Z').getTime();
  const b = new Date(toStr + 'T00:00:00Z').getTime();
  return Math.round((b - a) / 86400000);
}

const MESES = [
  'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
  'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro',
];

export function formatDatePt(dateStr: string): string {
  const [y, m, d] = dateStr.split('-').map(Number);
  return `${d} de ${MESES[m - 1]} de ${y}`;
}

export function formatDateShortPt(dateStr: string): string {
  const [, m, d] = dateStr.split('-').map(Number);
  return `${d} de ${MESES[m - 1]}`;
}

export type FaseAtual =
  | { tipo: 'agendado' }
  | { tipo: 'em_andamento'; diaAtual: number; totalDias: number }
  | { tipo: 'pronto_para_concluir' }
  | { tipo: 'concluido' };

export function faseAtual(run: ProtocolRun, items: ChecklistItem[]): FaseAtual {
  if (run.status === 'concluido') return { tipo: 'concluido' };

  const hoje = todayStr();
  const inicioFase = addDays(run.moon_date, Math.min(...items.map((i) => i.offsetStart)));

  if (hoje < inicioFase) return { tipo: 'agendado' };
  if (hoje > run.end_date) return { tipo: 'pronto_para_concluir' };

  const totalDias = daysBetween(inicioFase, run.end_date) + 1;
  const diaAtual = daysBetween(inicioFase, hoje) + 1;
  return { tipo: 'em_andamento', diaAtual, totalDias };
}

export function itemsDoDia(run: ProtocolRun, items: ChecklistItem[], dateStr?: string): ChecklistItem[] {
  const hoje = dateStr || todayStr();
  const offset = daysBetween(run.moon_date, hoje);
  return items.filter((i) => offset >= i.offsetStart && offset <= i.offsetEnd);
}
