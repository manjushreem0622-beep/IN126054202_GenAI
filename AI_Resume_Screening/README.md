# 🚀 AI Resume Screening System with LangChain & LangSmith

## 📌 Overview

This project implements an **AI-powered Resume Screening System** that evaluates candidates based on a given job description.

The system uses **LangChain** to build a modular pipeline and **LangSmith** for tracing and debugging. It analyzes resumes, compares them with job requirements, assigns a score, and provides clear explanations.

---

## 🎯 Objective

* Automate resume evaluation using AI
* Extract skills, tools, and experience
* Match candidate profiles with job requirements
* Generate a **fit score (0–100)**
* Provide **explainable outputs**
* Enable **pipeline tracing using LangSmith**

---

## ⚙️ Tech Stack

* Python
* LangChain
* LangSmith
* Groq API (LLM)
* VS Code

---

## 🏗️ Project Structure

```
AI_Resume_Screening/
│
├── chains/
│   ├── extract_chain.py
│   ├── match_chain.py
│   ├── score_chain.py
│   └── explain_chain.py
│
├── data/
│   ├── job_description.txt
│   ├── strong_resume.txt
│   ├── average_resume.txt
│   └── weak_resume.txt
│
├── prompts/
│   ├── extract_prompt.py
│   ├── match_prompt.py
│   ├── score_prompt.py
│   └── explain_prompt.py
│
├──.gitignore
├──README.md
├── main.py
└── requirements.txt
```

---

## 🔄 Pipeline Flow

```
Resume → Skill Extraction → Matching → Scoring → Explanation → LangSmith Tracing
```

---

## 🧠 Features

* ✔ Skill, tool, and experience extraction
* ✔ Resume-to-job matching
* ✔ Intelligent scoring system (0–100)
* ✔ Explainable AI outputs
* ✔ Modular LangChain pipeline
* ✔ Error handling and JSON validation
* ✔ Debug case testing
* ✔ LangSmith tracing for monitoring

---

## 🧪 Test Cases

The system evaluates:

1. **Strong Candidate** → High match → High score
2. **Average Candidate** → Partial match → Medium score
3. **Weak Candidate** → Low match → Low score
4. **Debug Candidate** → Edge case testing

---

## 📊 Sample Output

```
Strong Candidate → 100/100  
Average Candidate → 30/100  
Weak Candidate → 0/100  
Debug Candidate → ~10–20/100  
```

---

## 📸 Screenshots

Include the following screenshots:

* Terminal outputs (Strong, Average, Weak)
* Debug case output
* LangSmith run list
* LangSmith pipeline trace

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-link>
cd AI_Resume_Screening
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Configure `.env`

```
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai-resume-screening
```

### 5️⃣ Run Project

```
python main.py
```

---

## 🔍 LangSmith Tracing

LangSmith is used to:

* Track each pipeline step
* Debug incorrect outputs
* Monitor model behavior

---

## 🚧 Challenges Faced

* Handling invalid JSON outputs from LLM
* Preventing hallucination
* Designing structured prompts
* Ensuring stable pipeline execution

---

## 💡 Key Learnings

* Building modular AI pipelines using LangChain
* Importance of prompt engineering
* Handling real-world LLM output issues
* Debugging using LangSmith
* Designing explainable AI systems

---

## 🌟 Conclusion

This project demonstrates how AI can assist recruiters by automating resume screening while maintaining transparency through explainable outputs and tracing.

---

## 🔗 Author

**Manjushree M**

---
