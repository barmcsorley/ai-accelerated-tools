# ⚡ AI-Accelerated Engineering Labs

> **Experimentation Log:** Exploring the efficacy of LLM-integrated development environments (Cursor, Antigravity) in reducing Time-to-MVP for internal tooling.

## 🎯 Purpose
This repository serves as a monorepo for utility applications and proofs-of-concept built using an **AI-First** workflow.
* **Role:** Architect & Lead (Human)
* **Code Generation:** Cursor (Claude 3.5 Sonnet / GPT-4o)
* **Infrastructure:** Docker on UGreen NAS (GitOps)

## 📂 Projects

### 1. Sovereign RAG Ingestor (`/apps/rag-ingestor`)
A Python-based pipeline that watches a local directory of engineering documentation (Markdown/PDF), generates embeddings via **Ollama (nomic-embed-text)**, and stores them in a self-hosted **ChromaDB**.
* **Tech:** Python, LangChain, ChromaDB, Docker.
* **Goal:** Enable fully offline, private semantic search.

### 2. Lab Inventory (`/apps/inventory-prototype`)
A rapid prototype built in <45 minutes using "Vibe Coding" techniques. It visualises the status of home lab containers and hardware metrics.
* **Tech:** Streamlit, Python, Docker API.

## 🛡️ Security & CI/CD
* **Supply Chain:** Dependencies managed via Renovate.
* **Vulnerability Scanning:** Continuous auditing via **Mend**.
* **Deployment:** Images built via GitHub Actions and deployed to private registry.

* /
├── .github
│   └── workflows
│       └── security-scan.yml   # MEND/Renovate integration
├── apps
│   ├── rag-ingestor            # Python script to feed your Vector DB
│   │   ├── src/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── inventory-prototype     # A "Vibe Coded" Streamlit app
│       ├── src/
│       └── Dockerfile
├── deployment
│   └── docker-compose.yml      # How to run this entire suite locally
├── README.md                   # The Manifesto
└── .gitignore                  # Python/Docker standard ignores
