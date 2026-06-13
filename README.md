# 🚀 ResumeFit AI
### ATS Matching & CV Optimization System

> **Final Project — Ruangguru AI Engineering Bootcamp Batch 11**
> Bernard Lokasasmita

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

**ResumeFit AI** is an end-to-end AI application that helps job seekers understand exactly why their CV isn't passing ATS (Applicant Tracking System) filters — and gives them actionable steps to fix it.

Most job seekers send generic CVs without knowing which keywords are missing, which skills are misaligned, or why the wording isn't landing. ResumeFit AI solves this with a **4-layer hybrid AI scoring engine** that combines statistical NLP, semantic vector search, and generative AI into a single, easy-to-use app.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **ATS Match Score** | Overall CV-to-JD compatibility score (0–100%) |
| 📊 **4-Layer Hybrid Scoring** | TF-IDF + Pinecone Semantic + Keyword Coverage + Skill Match |
| 🗄️ **Vector Database Matching** | Semantic similarity via Pinecone — captures meaning, not just keywords |
| 🔍 **12-Aspect CV Evaluation** | LLM-powered deep analysis across 12 quality dimensions |
| ⚡ **Impact Language Analysis** | Detects weak verbs, buzzwords, and missing quantified achievements |
| 📋 **ATS Formatting Check** | Flags multi-column layouts, images, tables, missing sections |
| 🤖 **AI CV Rewrite** | Smart rewrite: tailors CV if match ≥60%, enhances overall quality if <60% |
| 📥 **Export** | Download full report as `.docx` or `.txt` |

---

## 🧠 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    ResumeFit AI                          │
│                                                          │
│  INPUT                                                   │
│  ┌──────────┐    ┌──────────────────┐                   │
│  │ CV (PDF) │    │ Job Description  │                   │
│  └────┬─────┘    └────────┬─────────┘                   │
│       │                   │                              │
│  LAYER 2: Processing      │                              │
│  ┌────▼─────────────────▼─────────┐                     │
│  │  PDF Extractor → Text Cleaner  │                     │
│  │  Skill Extractor → Keywords    │                     │
│  └──────────────┬─────────────────┘                     │
│                 │                                        │
│  LAYER 3: Analysis Engine                                │
│  ┌──────────────▼─────────────────────────────────┐     │
│  │  Statistical  │  Semantic    │  Rule-Based      │     │
│  │  TF-IDF       │  Pinecone    │  Keyword/Skill   │     │
│  │  Cosine Sim   │  Embeddings  │  Gap Detection   │     │
│  └──────────┬────┴──────┬───────┴──────────────────┘     │
│             │  Program  │                                 │
│             │ Ingestion │ Model Embedding                 │
│             └────────►  Vector Database (Pinecone)        │
│                                                          │
│  LLM Layer (Groq / OpenAI)                              │
│  ┌─────────────────────────────────────────────────┐    │
│  │  12-Aspect Evaluation  │  Impact Language        │    │
│  │  CV Rewrite Suggestion │  Career Recommendation  │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  LAYER 4: Output                                         │
│  Dashboard │ 12-Aspect │ AI Rewrite │ Format Check │ Export │
└─────────────────────────────────────────────────────────┘
```

---

## 📐 Scoring Formula

ResumeFit AI uses a **weighted hybrid formula** combining 4 layers:

```
Final Score = 0.4 × TF-IDF  +  0.3 × Pinecone  +  0.2 × Keywords  +  0.1 × Skills
```

| Component | Weight | Method |
|---|---|---|
| TF-IDF Cosine Similarity | 40% | `sklearn` TfidfVectorizer + cosine similarity |
| Pinecone Semantic Similarity | 30% | `sentence-transformers` embeddings + Pinecone vector search |
| Keyword Coverage | 20% | `∣KJ ∩ KR∣ / ∣KJ∣ × 100` |
| Skill Match | 10% | Rule-based dictionary matching |

> **Score Guide:** 🟢 75–100% Excellent &nbsp;|&nbsp; 🔵 55–75% Good &nbsp;|&nbsp; 🟡 35–55% Moderate &nbsp;|&nbsp; 🔴 0–35% Needs Work

---

## 🏗️ Tech Stack

| Category | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **UI** | Streamlit |
| **Statistical NLP** | Scikit-learn (TF-IDF, Cosine Similarity) |
| **Semantic Search** | Sentence-Transformers (`all-MiniLM-L6-v2`) |
| **Vector Database** | Pinecone (Serverless) |
| **LLM** | Groq (`llama-3.1-8b-instant`) — free default |
| **LLM (optional)** | OpenAI (`gpt-3.5-turbo`, `gpt-4o-mini`, `gpt-4o`) |
| **PDF Extraction** | PyPDF |
| **Visualization** | Plotly (gauge, radar, bar charts) |
| **Export** | python-docx |
| **Deployment** | Google Colab + ngrok |

---

## 🚀 Quick Start (Google Colab)

### 1. Clone / Download

```bash
git clone https://github.com/benloImA0G/AI-Boot-Camp-batch-11.git
```

Or download `ResumeFit AI Bernard L v1.ipynb` directly.

### 2. Set Up Secrets in Colab

In Google Colab → click the 🔑 **Secrets** icon (left sidebar) → add:

| Secret Name | Value | Required? |
|---|---|---|
| `NGROK_AUTH_TOKEN` | From [ngrok.com](https://ngrok.com) | ✅ Yes |
| `GROQ_API_KEY` | From [console.groq.com](https://console.groq.com) — **free** | ✅ Yes |
| `PINECONE_API_KEY` | From [pinecone.io](https://pinecone.io) — **free** | ✅ Yes |

### 3. Run the Notebook

1. Open the `.ipynb` file in Google Colab
2. Run **Cell 1** → writes `app.py`
3. Run **Cell 2** → installs dependencies, starts Streamlit, generates public URL
4. Click the ngrok URL to open the app

---

## 📖 How to Use

1. **Upload your CV** as a PDF file
2. **Paste the Job Description** you're applying for
3. Click **"Analyze My CV — Hybrid AI"**
4. Explore the 5 tabs:
   - 📊 **Dashboard** — overall scores, skill match, radar chart
   - 🔍 **12-Aspect Analysis** — deep breakdown with tips per aspect
   - 🤖 **AI-Optimized CV** — rewritten sections tailored to the job
   - ⚡ **Impact & Format** — weak verbs, buzzwords, ATS compatibility
   - 📥 **Export** — download full report

---

## 🔍 12 CV Evaluation Aspects

| # | Aspect | Category |
|---|---|---|
| 1 | Overall Impression | General |
| 2 | Contact Information | General |
| 3 | Consistent & Error-free | General |
| 4 | Relevant Skills | Competency |
| 5 | Professional Summary | Competency |
| 6 | Work Experience | Competency |
| 7 | Achievements | Competency |
| 8 | Education & Certification | Background |
| 9 | Organizational Activity | Background |
| 10 | Additional Sections | Background |
| 11 | Keywords Optimization | ATS |
| 12 | Career Recommendation | ATS |

---

## ⚡ Impact Language & ATS Format Checks

### Impact Language
- Detects **weak verbs**: "responsible for", "assisted", "helped", "worked on"
- Detects **buzzwords**: "results-driven", "self-starter", "passionate", "synergy"
- Checks for **quantified achievements** (%, $, numbers)
- LLM-powered Impact Score (0–100) with specific actionable tip

### ATS Formatting
- 🖼️ Image/graphic detection (ATS cannot read images)
- 📄 Page count check (1–2 pages recommended)
- ⚠️ Multi-column layout detection
- ⚠️ Table detection (breaks ATS parsing)
- ✅ Required sections check (Experience, Education, Skills)
- ✅ Contact information check

---

## 📁 Project Structure

```
resumefit-ai/
│
├── ResumeFit AI Bernard L v1.ipynb   # Main Colab notebook
├── app.py                             # Streamlit app (generated by Cell 1)
└── README.md                          # This file
```

---

## 🔄 Future Roadmap

| Version | Features |
|---|---|
| **V2.0** | Multi-job comparison, full Bahasa Indonesia support |
| **V3.0** | Job recommendation engine, CV auto-template generation |
| **V4.0** | Analysis history, public web deployment |
| **V5.0** | LinkedIn, JobStreet, and job portal integration |

---

## 👨‍💻 Author

**Bernard Lokasasmita**
Final Project — Ruangguru AI Engineering Bootcamp Batch 11

> *"AI yang baik bukan hanya yang akurat di notebook — tetapi yang bisa memberi nilai nyata kepada pengguna akhir."*
> ("Good AI is not just accurate in a notebook — it must deliver real value to end users.")

---

## 📄 License

MIT License — free to use, modify, and distribute.
