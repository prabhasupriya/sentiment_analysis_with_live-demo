export const connectWebSocket = (onMessage, onError) => {
  const ws = new WebSocket("ws://127.0.0.1:8000/ws/sentiment");

  ws.onopen = () => {
    console.log("✅ FRONTEND: WebSocket connected");
  };

  ws.onmessage = (e) => {
    const data = JSON.parse(e.data);
    console.log("📩 WS MESSAGE RECEIVED:", data); // 👈 IMPORTANT
    onMessage(data);
  };

  ws.onerror = (err) => {
    console.error("❌ WebSocket error", err);
    if (onError) onError(err);
  };

  ws.onclose = () => {
    console.warn("⚠️ WebSocket closed");
  };

  return ws;
};
