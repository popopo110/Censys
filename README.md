# 🔎 Censys Summarizer

A full-stack demo project that uses **FastAPI** + a simple **frontend UI** to summarize [Censys](https://censys.io/) host scan data.  

- **Purpose**:  
  The app demonstrates how to build a lightweight AI-agentic service:  
  1. Ingest raw host records (JSON).  
  2. Pass them to a summarization API/LLM backend.  
  3. Display concise summaries in the browser.  

It was built as a take-home AI Engineer project, with emphasis on **frontend + backend integration**, **API design**, and **deployment to GitHub Pages** (frontend) with a separate FastAPI backend.

---

## 📂 Project Tree
Download the package and run in terminal
├── main.py # FastAPI backend (API + static serving)
├── index.html # Frontend UI (simple HTML + JS)
├── hosts_dataset.json # Sample Censys host dataset
├── summaries.csv # Example CSV output of summaries
├── summaries.jsonl # Example JSONL output of summaries
├── requirements.txt # Python dependencies
└── Procfile # Start command (for Render/Railway)

## Run locally
git clone https://github.com/<your-username>/Censys.git
cd Censys
pip install -r requirements.txt
uvicorn main:app --reload --port 8000


## Run Codespace
1. Choose Code from repo
2. Select CodeSpace -> Create CodeSpace in main 
3. In terminal run: 
"pip install fastapi uvicorn[standard] pydantic>=2
uvicorn main:app --host 0.0.0.0 --port 8000"
