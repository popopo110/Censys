# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

app = FastAPI()

# (Dev) CORS: safe even if same-origin; keep for flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----- API types & route -----
class Record(BaseModel):
    ip: Optional[str] = None
    open_ports: List[int] = Field(default_factory=list)
    location: Optional[Dict[str, Any]] = None
    services: List[Dict[str, Any]] = Field(default_factory=list)

class BatchReq(BaseModel):
    records: List[Record]
    model: Optional[str] = "gpt-4o-mini"
    temperature: Optional[float] = 0.2

@app.post("/api/summarize-batch")
def summarize_batch(req: BatchReq):
    out = []
    for r in req.records:
        out.append({
            **r.model_dump(),
            "summary": {"text": f"Host {r.ip or 'unknown'} exposes {len(r.open_ports)} port(s)."}
        })
    return {"records": out}

# ----- Frontend (index.html) -----
@app.get("/")
def home():
    return FileResponse("index.html")

# Optionally serve other assets (css/js) from /static
app.mount("/static", StaticFiles(directory="."), name="static")
