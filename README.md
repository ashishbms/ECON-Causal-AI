# EconCausalAI – 3-Mode Architecture

## 📌 Overview

EconCausalAI is an AI-powered platform for economic policy analysis that integrates:

- Causal Discovery (NOTEARS, PC, GES)
- Agent-Based Modeling (100K–10M agents)
- Reinforcement Learning (policy optimization)
- Natural Language Interface (fine-tuned LLM)

It provides three specialized interfaces built on a unified computational core.

---

# 🧠 Platform Modes

## 1️⃣ Curated Mode
For policy analysts who need quick insights.

- Pre-processed datasets
- Workflow templates
- One-click analysis
- Auto-generated reports

**Example:**  
> "What happens if we raise interest rates to 5%?"

---

## 2️⃣ Sandbox Mode
For researchers who need full control.

- Python SDK
- JupyterHub notebooks
- Custom datasets
- Custom model experimentation

**Example:**  
> Testing novel monetary policy rules

---

## 3️⃣ AI Assistance Mode
Conversational AI interface for all users.

- Fine-tuned LLM trained on economic corpus
- Natural language queries
- Tool orchestration

**Example:**  
> "Compare fiscal stimulus vs infrastructure spending"

---

# 🏗️ Key Architectural Decisions

- Single unified computational core
- Multi-interface abstraction layer
- Fine-tuned LLM on 13K+ economic PDFs
- Kubernetes-based deployment
- 5-layer hierarchical pipeline
- Production-grade security and monitoring

---

# 📊 Critical Data Requirements

## 1️⃣ PDF Corpus (Available ✅)

- 13,000+ documents
- 27GB data
- Used for LLM fine-tuning
- Contains economic research & policy reports

## 2️⃣ Structured Datasets (To Be Collected ❗ CRITICAL)

- Target: 500+ curated datasets
- Sources: FRED, World Bank, IMF, OECD, ECB
- Timeline: 2–3 months
- Required for Curated Mode functionality

⚠️ Without structured datasets, the platform cannot function.

---

# 📚 Documentation Structure

## High-Level Design (HLD)

- Executive Summary & Vision
- System Architecture
- Data Architecture
- AI Assistance Mode Design
- Sandbox Mode Design
- Curated Mode Design
- Deployment Architecture
- Success Metrics
- Roadmap & Phasing
- Data Collection Guide (Critical)
- Future Work


# 🛠️ Tech Stack

## Backend
- Python 3.11
- gRPC
- FastAPI
- PostgreSQL
- TimescaleDB
- Redis
- Ray

## Frontend
- React.js (Curated Mode)
- JupyterLab (Sandbox Mode)
- WebSocket (AI Chat)

## Infrastructure
- Kubernetes
- Docker
- AWS / GCP / Azure
- S3-compatible storage

## ML / AI
- NOTEARS (Causal Discovery)
- FLAME GPU (ABM Simulation)
- Conservative Q-Learning (RL)
- Claude 3.5 Sonnet (Fine-tuned)




# 👨‍🎓 Project Information

**Project:** BMSCE Capstone – EconCausalAI  
**Institution:** B.M.S. College of Engineering, Bangalore  
**Version:** 2.0  
**Last Updated:** November 2025  
**Status:** Ready for Implementation  

---

## 📄 License

This project is developed as part of a capstone initiative and may be updated as architecture evolves.
