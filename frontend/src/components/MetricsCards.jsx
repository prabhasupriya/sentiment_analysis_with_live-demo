export default function MetricsCards({ metrics }) {
  const items = [
    { label: "Total", value: metrics.total },
    { label: "Positive", value: metrics.positive },
    { label: "Negative", value: metrics.negative },
    { label: "Neutral", value: metrics.neutral },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      {items.map((item) => (
        <div
          key={item.label}
          className="bg-gray-800 rounded-lg p-4 text-center"
        >
          <p className="text-sm text-gray-400">{item.label}</p>
          <p className="text-xl font-bold">{item.value}</p>
        </div>
      ))}
    </div>
  );
}
