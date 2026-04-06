# CSV Search Engine (Optimized)

## 📌 Overview
This project is a high-performance search engine built using Python.  
It processes large CSV datasets (5000+ rows) by converting them into a graph structure and performing ultra-fast searches.

## 🚀 Features
- Handles large datasets (5000+ nodes)
- Graph-based data structure
- Optimized search using direct mapping
- Instant path retrieval
- Execution time tracking
- Input validation (detects invalid nodes)

## 🧠 Algorithm
- Graph Representation
- Direct Mapping Optimization
- Inspired by Breadth-First Search (BFS)

## ⚡ Performance
- Near O(n) preprocessing
- Near O(1) search time

## 📂 Project Structure
CSV_Search_Engine/
│── data/
│   └── data.csv
│── src/
│   └── search_engine.py
│── generate_data.py
│── README.md

## ▶️ How to Run

```bash
python generate_data.py
python src/search_engine.py