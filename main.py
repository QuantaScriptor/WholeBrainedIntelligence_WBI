
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import numpy as np
from typing import List, Dict

app = FastAPI(title="WholeBrainedIntelligence API")

class InputData(BaseModel):
    text: str
    features: List[float] = None

@app.get("/")
async def root():
    return {"message": "WholeBrainedIntelligence API", "status": "active"}

@app.post("/analyze")
async def analyze(data: InputData):
    try:
        # Basic analysis example
        # Store last 5 analyses
        if not hasattr(app, 'analysis_history'):
            app.analysis_history = []
        
        current_analysis = {
            "text": data.text,
            "input_length": len(data.text),
            "complexity_score": np.random.random(),  # Placeholder
            "sentiment": np.random.choice(["positive", "negative", "neutral"]),
            "confidence": round(np.random.random(), 2)
        }
        
        app.analysis_history.insert(0, current_analysis)
        app.analysis_history = app.analysis_history[:5]  # Keep only last 5
        
        response = {
            **current_analysis,
            "history": app.analysis_history[1:]  # Exclude current analysis
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
