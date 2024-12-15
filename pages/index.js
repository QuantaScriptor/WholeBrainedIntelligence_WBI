
import { motion } from 'framer-motion'
import { useState } from 'react'

export default function Home() {
  const [input, setInput] = useState('')
  const [result, setResult] = useState(null)

  const analyzeText = async () => {
    const response = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: input })
    })
    const data = await response.json()
    setResult(data)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white">
      <main className="container mx-auto px-4 py-20">
        <motion.h1 
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="text-6xl font-bold text-center mb-8"
        >
          WholeBrainedIntelligence
        </motion.h1>
        
        <div className="max-w-3xl mx-auto space-y-8">
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="bg-white/10 p-6 rounded-lg backdrop-blur-lg"
          >
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              className="w-full h-32 bg-black/50 rounded p-4 text-white"
              placeholder="Enter your text for analysis..."
            />
            <button
              onClick={analyzeText}
              className="mt-4 px-6 py-2 bg-blue-600 rounded-full hover:bg-blue-700 transition-colors"
            >
              Analyze
            </button>
          </motion.div>

          {result && (
            <motion.div 
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              className="bg-white/10 p-6 rounded-lg backdrop-blur-lg"
            >
              <h2 className="text-xl font-semibold mb-4">Analysis Results</h2>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <p className="text-gray-400">Complexity Score</p>
                  <p className="text-2xl">{result.complexity_score.toFixed(2)}</p>
                </div>
                <div>
                  <p className="text-gray-400">Sentiment</p>
                  <p className="text-2xl capitalize">{result.sentiment}</p>
                </div>
                <div>
                  <p className="text-gray-400">Confidence</p>
                  <p className="text-2xl">{(result.confidence * 100).toFixed(0)}%</p>
                </div>
              </div>
            </motion.div>
          )}
        </div>
      </main>
    </div>
  )
}
