export default function RecentPosts({ posts }) {
  return (
    <div className="bg-gray-800 rounded-lg p-4 h-80 overflow-y-auto">
      <h3 className="text-lg font-semibold mb-3">Recent Posts Feed</h3>

      {posts.length === 0 && (
        <p className="text-gray-400">Live sentiment updates streaming...</p>
      )}

      {posts.map((post, i) => (
        <div key={i} className="border-b border-gray-700 py-2">
          <p className="text-sm">{post.content}</p>
          <span className="text-xs text-gray-400">
            Sentiment: {post.sentiment}
          </span>
        </div>
      ))}
    </div>
  );
}
