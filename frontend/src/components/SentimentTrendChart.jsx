import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

export default function SentimentTrendChart({ data }) {
  if (!data.length) {
    return (
      <div className="bg-gray-800 p-4 rounded-lg">
        <h3 className="text-lg font-semibold">
          Sentiment Trend (Last 24 Hours)
        </h3>
        <p className="text-gray-400">No data available</p>
      </div>
    );
  }

  return (
    <div className="bg-gray-800 p-4 rounded-lg">
      <h3 className="text-lg font-semibold mb-4">
        Sentiment Trend (Last 24 Hours)
      </h3>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="positive" stroke="#10b981" />
          <Line type="monotone" dataKey="negative" stroke="#ef4444" />
          <Line type="monotone" dataKey="neutral" stroke="#6b7280" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
