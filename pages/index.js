
import { motion } from 'framer-motion'
import { useState } from 'react'
import { Line } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default function Home() {
  const [input, setInput] = useState('')
  const [mode, setMode] = useState('analyze')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [filter, setFilter] = useState('all')

  const modes = {
    analyze: "Pattern Recognition & Self-Awareness",
    simulate: "Counterfactual Simulation",
    learn: "Learning from Experience",
    interact: "Empathic Interaction"
  }

  const analyzeText = async () => {
    if (!input.trim()) return
    setLoading(true)
    try {
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: input, mode })
      })
      const data = await response.json()
      setResult(data)
    } catch (error) {
      console.error('Analysis failed:', error)
    }
    setLoading(false)
  }

  const exportResults = (data) => {
    const csvContent = "data:text/csv;charset=utf-8," + 
      "Text,Mode,Complexity Score,Sentiment,Confidence\n" +
      data.map(item => 
        `"${item.text}",${item.mode},${item.complexity_score},${item.sentiment},${item.confidence}`
      ).join("\n")
    const encodedUri = encodeURI(csvContent)
    const link = document.createElement("a")
    link.setAttribute("href", encodedUri)
    link.setAttribute("download", "wbi_analysis.csv")
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
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
              <select
                value={mode}
                onChange={(e) => setMode(e.target.value)}
                className="w-full mb-4 bg-black/30 rounded-lg p-4 text-white"
              >
                {Object.entries(modes).map(([key, value]) => (
                  <option key={key} value={key}>{value}</option>
                ))}
              </select>
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
                  {loading ? 'Processing...' : 'Analyze'}
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
                    Analysis Results
                  </h2>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div className="bg-white/5 rounded-lg p-4">
                      <p className="text-gray-400 text-sm">Mode</p>
                      <p className="text-xl font-semibold mt-1">{result.mode}</p>
                    </div>
                    <div className="bg-white/5 rounded-lg p-4">
                      <p className="text-gray-400 text-sm">Sentiment</p>
                      <p className="text-xl font-semibold mt-1 capitalize">{result.sentiment}</p>
                    </div>
                    <div className="bg-white/5 rounded-lg p-4">
                      <p className="text-gray-400 text-sm">Confidence</p>
                      <p className="text-xl font-semibold mt-1">{result.confidence * 100}%</p>
                    </div>
                  </div>
                  
                  <div className="mt-6">
                    <h3 className="text-lg font-semibold mb-4">Insights</h3>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                      {Object.entries(result.insights).map(([key, values]) => (
                        <div key={key} className="bg-white/5 p-4 rounded-lg">
                          <p className="text-sm text-gray-400 capitalize">{key}</p>
                          <ul className="mt-2 space-y-1">
                            {values.map((value, index) => (
                              <li key={index} className="text-sm">{value}</li>
                            ))}
                          </ul>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="bg-white/5 backdrop-blur-lg rounded-xl p-6 border border-white/10 shadow-xl">
                  <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
                      Analysis History
                    </h2>
                    <button
                      onClick={() => exportResults([result, ...result.history])}
                      className="bg-white/5 px-4 py-2 rounded-lg text-sm hover:bg-white/10"
                    >
                      Export Results
                    </button>
                  </div>
                  <div className="space-y-4">
                    {[result, ...result.history].map((item, index) => (
                      <div key={index} className="bg-white/5 p-4 rounded-lg">
                        <p className="text-sm text-gray-400">Text: {item.text.substring(0, 100)}...</p>
                        <div className="grid grid-cols-3 gap-4 mt-2">
                          <p className="text-sm">Mode: {item.mode}</p>
                          <p className="text-sm">Sentiment: {item.sentiment}</p>
                          <p className="text-sm">Confidence: {item.confidence * 100}%</p>
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
