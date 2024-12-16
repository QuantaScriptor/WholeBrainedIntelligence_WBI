
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import numpy as np
from typing import List, Dict

app = FastAPI(title="WholeBrainedIntelligence API")

class InputData(BaseModel):
    text: str
    features: List[float] = None
    mode: str = "analyze"  # analyze, simulate, learn, interact

@app.get("/")
async def root():
    return {"message": "WholeBrainedIntelligence API", "status": "active"}

@app.post("/analyze")
async def analyze(data: InputData):
    try:
        modes = {
            "analyze": "Pattern Recognition & Self-Awareness",
            "simulate": "Counterfactual Simulation",
            "learn": "Learning from Experience",
            "interact": "Empathic Interaction"
        }

        current_analysis = {
            "text": data.text,
            "mode": modes.get(data.mode, "analyze"),
            "complexity_score": round(np.random.random(), 2),
            "sentiment": np.random.choice(["positive", "negative", "neutral"]),
            "confidence": round(np.random.random(), 2),
            "insights": {
                "patterns": ["Pattern 1", "Pattern 2"],
                "predictions": ["Prediction 1", "Prediction 2"],
                "recommendations": ["Recommendation 1", "Recommendation 2"]
            }
        }
        
        if not hasattr(app, 'analysis_history'):
            app.analysis_history = []
            
        app.analysis_history.insert(0, current_analysis)
        app.analysis_history = app.analysis_history[:5]
        
        return {
            **current_analysis,
            "history": app.analysis_history[1:]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, access_log=False)
