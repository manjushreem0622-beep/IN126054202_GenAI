# 🚀 RAG-Based Customer Support Assistant  
### Using LangGraph & Human-in-the-Loop (HITL)

---

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant that can:

- Understand user queries  
- Retrieve relevant information from a PDF knowledge base  
- Generate accurate and context-aware responses  
- Escalate queries to a human when confidence is low  

This system goes beyond a basic chatbot by incorporating **retrieval, reasoning, and decision-making capabilities**.

---

## 🎯 Problem Statement

Traditional chatbots often fail because:

- They rely only on pre-trained knowledge  
- They generate inaccurate or hallucinated responses  
- They cannot handle complex queries  

To address this, this project uses **RAG architecture combined with workflow control and human escalation**.

---

## 🧠 What is RAG?

**RAG (Retrieval-Augmented Generation)** combines:

- 🔍 Information Retrieval  
- 🤖 Text Generation  

Instead of generating answers blindly, the system:

- Retrieves relevant information from documents  
- Uses that information to generate accurate responses  

---

## 🏗️ System Architecture

The system consists of two main pipelines:

### 📥 Document Pipeline
- Load PDF document  
- Extract text  
- Split into chunks  
- Generate embeddings  
- Store in vector database (ChromaDB)  

### 📤 Query Pipeline
- User inputs query  
- Convert query into embedding  
- Retrieve relevant chunks  
- Pass to LLM  
- Generate response  
- Apply decision logic (Answer / Escalate)  

---

## ⚙️ Key Components

- 📄 Document Loader  
- ✂️ Text Chunking Module  
- 🔢 Embedding Model  
- 🗂️ Vector Database (ChromaDB)  
- 🔍 Retriever  
- 🤖 LLM (Language Model)  
- 🔄 LangGraph Workflow Engine  
- 🧭 Routing Logic  
- 👤 Human-in-the-Loop (HITL)  

---

## 🔁 Workflow (LangGraph)

The system follows a structured workflow:

