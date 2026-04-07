# CSV Search Engine 🚀

## 📌 General Overview & Introduction (GOI)
This project is a high-performance CSV search engine built using Python. It is designed to efficiently process large datasets (5000+ nodes) by converting the data into a graph structure.

Instead of performing repeated searches through the dataset, the system uses an optimized direct mapping technique, allowing near-instant retrieval of paths between nodes.

This project demonstrates how algorithm optimization and data structures can significantly improve performance when working with large-scale data.

---

## 📌 Overview
This project processes large CSV datasets by converting them into a graph structure and performing ultra-fast searches.

---

## 🚀 Features
- Handles large datasets (5000+ nodes)
- Graph-based data structure
- Optimized search using direct mapping
- Instant path retrieval
- Execution time tracking
- Input validation (detects invalid nodes)

---

## 🧠 Algorithm
- Graph Representation (Adjacency List)
- Direct Mapping Optimization
- Inspired by Breadth-First Search (BFS)

---

## ⚡ Performance
- Near O(n) preprocessing
- Near O(1) search time

---

## 📂 Project Structure
CSV_Search_Engine/
│── data/
│ └── data.csv
│── src/
│ └── search_engine.py
│── generate_data.py
│── README.md


---

## ▶️ How to Run


python generate_data.py
python src/search_engine.py


---

## 🧪 Example Input


Enter target node: N100


---

## ✅ Example Output


Path: N1 -> N2 -> ... -> N100
Execution Time: 0.000045 seconds


---

## 👨‍💻 Author
Austine