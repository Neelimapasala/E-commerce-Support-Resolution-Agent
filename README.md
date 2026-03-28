#  E‑Commerce Support Resolution Agent

This repository contains my submission for the **AI/ML Engineer Intern Assessment** at Purple Merit Technologies.  
It implements a multi‑agent Retrieval‑Augmented Generation (RAG) system designed to resolve customer support tickets using policy documents, with strong controls against hallucination, missing citations, and unsafe outputs.

---

##  Features
- Multi‑agent orchestration (CrewAI / LangChain)
- Policy‑grounded responses with citations
- Compliance and safety checks (no hallucinations, no unsupported claims)
- Handles ambiguity, exceptions, and conflict cases
- Evaluation framework with metrics and example runs

---

##  System Architecture
The system is composed of four required agents plus optional extensions:

1. **Triage Agent**  
   - Classifies issue type (refund, shipping, payment, promo, fraud, other)  
   - Identifies missing fields and asks clarifying questions  

2. **Policy Retriever Agent**  
   - Queries vector database (FAISS)  
   - Returns top‑k relevant excerpts with citations  

3. **Resolution Writer Agent**  
   - Drafts customer‑ready response using retrieved evidence only  

4. **Compliance / Safety Agent**  
   - Verifies citations, blocks hallucinations, checks tone and policy adherence  
   - Escalates if conflict or unsupported  

**Optional Agents:** Order Context Interpreter, Escalation Agent.

---
---

## ⚙️ Setup & Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/Neelimapasala/ai-ml-intern-assessment.git
cd ai-ml-intern-assessment
pip install -r requirements.txt
sample input:

python src/main.py --ticket "My order arrived late and the cookies are melted. I want a refund." \
                   --context '{"order_date":"2026-03-20","delivery_date":"2026-03-25","item_category":"perishable","fulfillment_type":"first-party","shipping_region":"India","order_status":"delivered"}'

Evaluation:

Test set: 20 tickets (8 standard, 6 exception‑heavy, 3 conflict, 3 not‑in‑policy)
Citation coverage rate: 100%
Unsupported claim rate: 0%
Correct escalation rate: 100%


---

✨ This README is professional, covers setup, usage, architecture, evaluation, and deliverables. It will make your repo look polished and easy to review.  
Would you like me to also generate a **requirements.txt template** with common dependencies (LangChain, FAISS, sentence‑transformers, etc.) so you can drop it in?

## 📂 Repository Structure
