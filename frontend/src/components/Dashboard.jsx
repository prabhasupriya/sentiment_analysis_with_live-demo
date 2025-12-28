import { useEffect, useState } from "react";
import DistributionChart from "./DistributionChart";
import SentimentTrendChart from "./SentimentTrendChart";
import RecentPosts from "./RecentPosts";
import MetricsCards from "./MetricsCards";
import { connectWebSocket } from "../services/api";

export default function Dashboard() {
  const [distribution, setDistribution] = useState({
    positive: 0,
    negative: 0,
    neutral: 0,
  });

  const [trendData, setTrendData] = useState([]);
  const [recentPosts, setRecentPosts] = useState([]);

  const [metrics, setMetrics] = useState({
    total: 0,
    positive: 0,
    negative: 0,
    neutral: 0,
  });

  const [status, setStatus] = useState("connecting");
  const [lastUpdate, setLastUpdate] = useState(null);

  useEffect(() => {
    const ws = connectWebSocket(
      (msg) => {
        console.log("📩 DASHBOARD RECEIVED:", msg);
        setStatus("connected");
        setLastUpdate(new Date().toLocaleTimeString());

        // ✅ BACKEND MESSAGE FORMAT
        if (msg.type === "sentiment") {
          const { positive, negative, neutral, timestamp } = msg;

          // PIE CHART
          setDistribution({ positive, negative, neutral });

          // METRICS
          setMetrics({
            total: positive + negative + neutral,
            positive,
            negative,
            neutral,
          });

          // LINE CHART
          setTrendData((prev) => [
            ...prev.slice(-20),
            {
              time: new Date(timestamp).toLocaleTimeString(),
              positive,
              negative,
              neutral,
            },
          ]);

          // RECENT POSTS (✅ THIS FIXES ESLINT)
          setRecentPosts((prev) => [
            {
              id: Date.now(),
              content: "Live sentiment update",
              sentiment:
                positive > negative
                  ? "positive"
                  : negative > positive
                  ? "negative"
                  : "neutral",
              timestamp,
            },
            ...prev.slice(0, 20),
          ]);
        }
      },
      () => {
        setStatus("disconnected");
      }
    );

    return () => ws.close();
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      {/* HEADER */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold">
          Real-Time Sentiment Analysis Dashboard
        </h1>

        <div className="flex gap-6 mt-2 text-sm">
          <span>
            Status:{" "}
            {status === "connected" && (
              <span className="text-green-400">● Live</span>
            )}
            {status === "connecting" && (
              <span className="text-yellow-400">● Connecting</span>
            )}
            {status === "disconnected" && (
              <span className="text-red-400">● Offline</span>
            )}
          </span>

          <span>
            Last Update:{" "}
            <span className="text-blue-400">
              {lastUpdate || "--:--:--"}
            </span>
          </span>
        </div>
      </div>

      {/* ROW 1 */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <DistributionChart data={distribution} />
        <RecentPosts posts={recentPosts} />
      </div>

      {/* ROW 2 */}
      <div className="mt-6">
        <SentimentTrendChart data={trendData} />
      </div>

      {/* ROW 3 */}
      <div className="mt-6">
        <MetricsCards metrics={metrics} />
      </div>
    </div>
  );
}
