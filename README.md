<div align="center">

# Tharun Kumar Gajula

**Product · Analytics · AI Systems**

Curated portfolio of **live product prototypes** and **8 end-to-end analytics architectures** spanning elder care, knowledge graphs, learning systems, credit risk, and quantitative modeling.

**Live portfolio:** [tharungajula.vercel.app](https://tharungajula.vercel.app)

</div>

---

## About This Repository

My background is not one straight line. It started in institutional credit risk workflows, grew through data pipelines and predictive modeling, and now extends into independent, full-stack AI product prototyping. The common thread: taking dense, ambiguous logic and turning it into systems people can actually use.

The portfolio is split into three parts:
1. **Current Build:** VIZIER, a personal multi-agent assistant, in active development.
2. **Live Product Prototypes:** Three concept operating systems, kept sharp and improved over time.
3. **Quantitative Analytics:** Structured architectures detailing end-to-end machine learning and risk models.

---

## 🔧 Current Build

### VIZIER — Personal Multi-Agent Assistant `(Work in Progress)`
A multi-agent assistant where a **LangGraph supervisor** routes requests across four specialists for calendar, email, research, and analysis, connected to real Gmail and Google Calendar through OAuth. Includes hybrid vector + keyword **RAG** (pgvector on Supabase), long-term memory across sessions, a custom **MCP server**, and an LLM gateway with automatic provider fallback via LiteLLM. Every write action goes through a **human-in-the-loop approval gate**: the agent proposes, I decide. Next up: approval inbox with audit logging, prompt-injection defenses, and Langfuse-based evals.

---

## 🚀 Live Product Prototypes

Exploratory web systems built with Next.js, Tailwind, and AI integrations to merge data, context, and operational workflows into cohesive products.

### [Parents Health OS](PASTE-LIVE-URL-HERE)
**Remote Elder-Care Console**
Built for Indian families caring for parents from a distance. Parents check in over WhatsApp with no app to learn, while the family dashboard tracks medications, vitals, and triage, and generates doctor-ready briefs. Local-first by design, with consent-based onboarding and a bounded, non-diagnostic AI automation layer.

### [Quant OS](https://quant-os.vercel.app)
**Spatial Knowledge Base for Quantitative Finance**
Markdown notes become an interactive force-directed graph with wikilinks, automated backlinks, KaTeX math rendering, and mastery tracking. Includes Vian AI, a terminal-style chatbot grounded strictly in the knowledge base as a deliberate hallucination guardrail.

### [Curiosity OS](https://curiosity-os.vercel.app)
**Digital Lab for Training Thinking Skills**
Runnable activity playbooks with evidence logging and a reflection workspace, curated learning paths, and a 3D causal knowledge map explored through Student, Mentor, and Builder lenses. Activities are run, not read.

---

## 📊 Featured Analytics Projects

| Project | Area | What it covers |
|---|---|---|
| **[Lending Club Credit Risk Masterclass](./brain/1_lending_club_credit_risk_masterclass.md)** | Credit Risk | End-to-end retail credit risk workflow covering **PD, LGD, EAD, Expected Loss, scorecards, validation, monitoring, CECL, and stress testing**. |
| **[Bank Churn Prediction with Neural Networks](./brain/5_bank_churn_neural_networks_masterclass.md)** | Banking / Retention Analytics | Binary classification using **neural networks, imbalance handling, dropout, optimizer comparison, ROC-AUC, and recall-focused decision logic**. |
| **[Employee Retention & Performance Analytics](./brain/6_employee_retention_tree_models_masterclass.md)** | HR Analytics / Tabular ML | Attrition modeling with **logistic regression, decision trees, random forests, feature engineering, grid search, and model comparison**. |
| **[Socio-Economic Household Classification](./brain/7_socio_economic_household_classification_masterclass.md)** | Large-Scale Tabular ML | Noisy real-world classification with **heavy preprocessing, missing-value handling, outlier treatment, PCA, SMOTE, random forests, and XGBoost**. |
| **[Twitter Sentiment Analysis with NLP](./brain/8_twitter_sentiment_nlp_masterclass.md)** | NLP / Text Analytics | Multi-class sentiment classification using **text cleaning, tokenization, lemmatization, CountVectorizer, TF-IDF, and Random Forests**. |
| **[CartPole Reinforcement Learning Masterclass](./brain/11_cartpole_reinforcement_learning_masterclass.md)** | Reinforcement Learning | Comparative RL study covering **REINFORCE, baseline subtraction, custom reward shaping, PPO, DQN, Actor-Critic, SAC, and Twin-Q**. |
| **[Antidiabetic Drug Prescription Forecasting](./brain/12_antidiabetic_drug_prescription_forecasting_masterclass.md)** | Time-Series Forecasting | Classical forecasting workflow using **STL decomposition, stationarity testing, SARIMA, rolling forecasts, baseline comparison, and MAPE**. |
| **[NIFTY 100 Portfolio Optimization](./brain/13_nifty100_portfolio_optimization_mpt_masterclass.md)** | Quant Finance / Portfolio Construction | Portfolio optimization covering **log returns, covariance, Monte Carlo portfolio weights, Sharpe-ratio selection, and efficient-frontier thinking**. |

---

## Core Skills Reflected Across the Projects

**Agentic AI (hands-on via VIZIER)**
LangGraph, Model Context Protocol (MCP), RAG with pgvector (hybrid search), LiteLLM model gateway, Google OAuth integrations, human-in-the-loop action design.

**Product & Systems Building**
Next.js (App Router), React, Tailwind CSS, FastAPI, Supabase, PostgreSQL, LLM integrations, structured prompts, spatial graph architectures.

**Risk & Quantitative Modeling**
Credit risk modeling (PD/LGD/EAD/Expected Loss), scorecards, cross-sectional equity strategy frameworks, turnover-controlled portfolio optimization, forecasting.

**Machine Learning & AI**
Logistic regression, ensembles (XGBoost, LightGBM), neural networks, reinforcement learning, NLP vectorization, model validation (KS, AUC, PSI).
