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
| 🤖 **AI CV Rewrite** | Smart rewrite: tailors CV if match >= 60%, enhances overall quality if < 60% |
| 📥 **Export** | Download full report as .docx or .txt |

---

## 🧠 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      ResumeFit AI                       │
│  INPUT                                                  │
│  ┌──────────┐          ┌──────────────────┐            │
│  │ CV (PDF) │          │ Job Description  │            │
│  └────┬─────┘          └────────┬─────────┘            │
│  LAYER 2: Processing                                    │
│  ┌────▼─────────────────▼─────────┐                    │
│  │ PDF Extractor → Text Cleaner   │                    │
│  │ Skill Extractor → Keywords     │                    │
│  └──────────────┬─────────────────┘                    │
│  LAYER 3: Analysis Engine                               │
│  ┌──────────────▼─────────────────────────────────┐    │
│  │ TF-IDF │ Pinecone Embeddings │ Keyword/Skill   │    │
│  └──────────┬────┴──────┬───────┴──────────────────┘   │
│             └────────► Vector Database (Pinecone)       │
│  LLM Layer (Groq / OpenAI)                              │
│  12-Aspect Evaluation | CV Rewrite | Career Advice      │
│  LAYER 4: Output                                        │
│  Dashboard │ 12-Aspect │ AI Rewrite │ Format │ Export   │
└─────────────────────────────────────────────────────────┘
```

---

## 📐 Scoring Formula

```
Final Score = 0.4 × TF-IDF + 0.3 × Pinecone + 0.2 × Keywords + 0.1 × Skills
```

| Component | Weight | Method |
|---|---|---|
| TF-IDF Cosine Similarity | 40% | sklearn TfidfVectorizer + cosine similarity |
| Pinecone Semantic Similarity | 30% | sentence-transformers + Pinecone vector search |
| Keyword Coverage | 20% | Intersection of job and resume keywords |
| Skill Match | 10% | Rule-based dictionary matching |

> **Score Guide:** 🟢 75–100% Excellent | 🔵 55–75% Good | 🟡 35–55% Moderate | 🔴 0–35% Needs Work

---

## 🏗️ Tech Stack

| Category | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **UI** | Streamlit |
| **Statistical NLP** | Scikit-learn (TF-IDF, Cosine Similarity) |
| **Semantic Search** | Sentence-Transformers (all-MiniLM-L6-v2) |
| **Vector Database** | Pinecone (Serverless) |
| **LLM** | Groq (llama-3.1-8b-instant) — free default |
| **LLM (optional)** | OpenAI (gpt-3.5-turbo, gpt-4o-mini, gpt-4o) |
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

### 2. Set Up Secrets in Colab

| Secret Name | Required? |
|---|---|
| NGROK_AUTH_TOKEN | Yes (free at ngrok.com) |
| GROQ_API_KEY | Yes (free at console.groq.com) |
| PINECONE_API_KEY | Yes (free at pinecone.io) |

### 3. Run the Notebook

1. Open ResumeFit_AI_Bernard_L_v1.ipynb in Google Colab
2. Run **Cell 1** — writes app.py
3. Run **Cell 2** — installs deps, starts Streamlit, generates public URL
4. Click the ngrok URL to open the app

---

## 📖 How to Use

1. Upload your CV as a PDF file
2. Paste the Job Description you are applying for
3. Click "Analyze My CV — Hybrid AI"
4. Explore the 5 tabs: Dashboard | 12-Aspect Analysis | AI-Optimized CV | Impact & Format | Export

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

## 📁 Project Structure

```
resumefit-ai/
├── ResumeFit_AI_Bernard_L_v1.ipynb  # Main Colab notebook
├── app.py                            # Streamlit app
└── README.md                         # This file
```

---

## 🔄 Future Roadmap

| Version | Features |
|---|---|
| V2.0 | Multi-job comparison, full Bahasa Indonesia support |
| V3.0 | Job recommendation engine, CV auto-template generation |
| V4.0 | Analysis history, public web deployment |
| V5.0 | LinkedIn, JobStreet, and job portal integration |

---

## 👨‍💻 Author

**Bernard Lokasasmita**
Final Project — Ruangguru AI Engineering Bootcamp Batch 11

> "AI yang baik bukan hanya yang akurat di notebook — tetapi yang bisa memberi nilai nyata kepada pengguna akhir."
> ("Good AI is not just accurate in a notebook — it must deliver real value to end users.")

---

## 📄 License

MIT License — free to use, modify, and distribute.
