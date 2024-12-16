
import { motion } from 'framer-motion'

import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

import { useState } from 'react'

export default function Home() {
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [filter, setFilter] = useState('all')

  const exportResults = (data) => {
    const csvContent = "data:text/csv;charset=utf-8," + 
      "Text,Complexity Score,Sentiment,Confidence\n" +
      data.map(item => 
        `"${item.text}",${item.complexity_score},${item.sentiment},${item.confidence}`
      ).join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "analysis_results.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const analyzeText = async () => {
    if (!input.trim()) return
    setLoading(true)
    try {
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: input })
      })
      const data = await response.json()
      setResult(data)
    } catch (error) {
      console.error('Analysis failed:', error)
    }
    setLoading(false)
  }

  return (
    <div className="min-h-screen bg-[#0A0A0F] text-white">
      <div className="absolute inset-0 bg-gradient-to-br from-purple-900/20 via-transparent to-blue-900/20" />
      <main className="relative container mx-auto px-4 py-12">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="max-w-4xl mx-auto"
        >
          <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent text-center mb-8">
            WholeBrainedIntelligence
          </h1>
          
          <motion.div 
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="space-y-6"
          >
            <div className="bg-white/5 backdrop-blur-lg rounded-xl p-6 border border-white/10 shadow-xl">
              <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="w-full h-40 bg-black/30 rounded-lg p-4 text-white placeholder-gray-400 focus:ring-2 focus:ring-blue-500 focus:outline-none resize-none"
                placeholder="Enter your text for analysis..."
              />
              <div className="mt-4 flex justify-end">
                <button
                  onClick={analyzeText}
                  disabled={loading || !input.trim()}
                  className={`px-6 py-2.5 rounded-lg font-medium transition-all duration-200 ${
                    loading || !input.trim()
                      ? 'bg-gray-600 cursor-not-allowed'
                      : 'bg-gradient-to-r from-blue-500 to-purple-500 hover:opacity-90'
                  }`}
                >
                  {loading ? 'Analyzing...' : 'Analyze'}
                </button>
              </div>
            </div>

            {result && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
              >
                <div className="bg-white/5 backdrop-blur-lg rounded-xl p-6 border border-white/10 shadow-xl">
                  <h2 className="text-xl font-semibold mb-6 bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
                    Latest Analysis
                  </h2>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className="bg-white/5 rounded-lg p-4">
                    <p className="text-gray-400 text-sm">Complexity Score</p>
                    <p className="text-2xl font-semibold mt-1">
                      {result.complexity_score?.toFixed(2) || 'N/A'}
                    </p>
                  </div>
                  <div className="bg-white/5 rounded-lg p-4">
                    <p className="text-gray-400 text-sm">Sentiment</p>
                    <p className="text-2xl font-semibold mt-1 capitalize">
                      {result.sentiment || 'N/A'}
                    </p>
                  </div>
                  <div className="bg-white/5 rounded-lg p-4">
                    <p className="text-gray-400 text-sm">Confidence</p>
                    <p className="text-2xl font-semibold mt-1">
                      {result.confidence ? `${(result.confidence * 100).toFixed(0)}%` : 'N/A'}
                    </p>
                  </div>
                </div>
                <div className="bg-white/5 backdrop-blur-lg rounded-xl p-6 border border-white/10 shadow-xl">
                  <h2 className="text-xl font-semibold mb-6 bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
                    Analysis History
                  </h2>
                  <div className="flex justify-between items-center mb-4">
                    <select 
                      onChange={(e) => setFilter(e.target.value)}
                      className="bg-white/5 rounded-lg p-2 text-sm"
                    >
                      <option value="all">All Results</option>
                      <option value="positive">Positive</option>
                      <option value="negative">Negative</option>
                      <option value="neutral">Neutral</option>
                    </select>
                    <button
                      onClick={() => exportResults(result.history)}
                      className="bg-white/5 px-4 py-2 rounded-lg text-sm hover:bg-white/10"
                    >
                      Export Results
                    </button>
                  </div>
                  <div className="space-y-4">
                    {result.history?.filter(item => 
                      filter === 'all' ? true : item.sentiment === filter
                    ).map((item, index) => (
                      <div key={index} className="bg-white/5 p-4 rounded-lg">
                        <p className="text-sm text-gray-400">Text: {item.text.substring(0, 100)}...</p>
                        <div className="grid grid-cols-3 gap-4 mt-2">
                          <p className="text-sm">Score: {item.complexity_score?.toFixed(2)}</p>
                          <p className="text-sm">Sentiment: {item.sentiment}</p>
                          <p className="text-sm">Confidence: {(item.confidence * 100).toFixed(0)}%</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </motion.div>
            )}
          </motion.div>
        </motion.div>
      </main>
    </div>
  )
}
