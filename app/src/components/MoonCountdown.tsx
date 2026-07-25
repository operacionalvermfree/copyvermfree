import { daysBetween, formatDateShortPt, todayStr } from '../lib/dates';

export default function MoonCountdown({ moonDate }: { moonDate: string }) {
  const dias = daysBetween(todayStr(), moonDate);

  if (dias <= 0) {
    return <p className="text-sm text-neutral-600">A lua nova deste ciclo é hoje 🌑</p>;
  }

  return (
    <p className="text-sm text-neutral-600">
      🌑 Próxima lua nova em <span className="font-semibold text-[var(--vf-green-dark)]">{dias} dia{dias === 1 ? '' : 's'}</span>{' '}
      · {formatDateShortPt(moonDate)}
    </p>
  );
}
