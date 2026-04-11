# CSV Search Engine 🚀

## 📌 General Overview & Introduction (GOI)

This project is a high-performance CSV Search Engine built using Python. It is designed to efficiently process large datasets (5000+ nodes) by converting the data into a graph structure.

Instead of repeatedly scanning the dataset, the system uses an optimized **direct mapping technique**, allowing near-instant retrieval of paths between nodes.

This project demonstrates how proper use of **data structures and algorithm optimization** can significantly improve performance when working with large-scale data.

---

## 🎯 Purpose

The goal of this project is to demonstrate how fast search operations can be achieved on large datasets using graph-based techniques and optimization strategies.

---

## 📌 Overview

The system reads a CSV file containing node relationships, builds a graph (adjacency list), and performs ultra-fast searches to find paths between nodes.

---

## 🚀 Features

* Handles large datasets (5000+ nodes)
* Graph-based data structure (Adjacency List)
* Optimized search using direct mapping
* Ultra-fast path retrieval
* Execution time tracking
* Input validation (detects invalid nodes)
* Simple GUI interface for user interaction

---

## 🧠 Algorithm & Approach

This project uses the following concepts:

* **Graph Representation**
  The CSV data is converted into an adjacency list.

* **Direct Mapping Optimization**
  Each node is mapped to its parent for faster lookup.

* **Search Strategy**
  Inspired by Breadth-First Search (BFS), but optimized to avoid repeated traversal.

---

## ⚡ Performance

* Preprocessing Time: O(n)
* Search Time: ~ O(1) (near constant time)
* Efficient even with large datasets

---

## 🖥️ GUI Interface

The project includes a simple graphical user interface (GUI).

Users can:

* Enter a target node
* Click search
* View the full path
* See execution time instantly

---

## 📂 Project Structure

CSV_Search_Engine/
│── data/
│   └── data.csv
│── src/
│   ├── search_engine.py
│   └── gui_app.py
│── generate_data.py
│── README.md

---

## 💻 How to Run on Your Local Machine

### 1. Clone the Repository

```bash
git clone https://github.com/Austin-dev7/CSV_Search_Engine.git
```

### 2. Navigate into the Project Folder

```bash
cd CSV_Search_Engine
```

### 3. Generate the Dataset

```bash
python generate_data.py
```

### 4. Run the Application

#### ▶️ Run GUI Version (Recommended)

```bash
python src/gui_app.py
```

#### ▶️ Run Terminal Version

```bash
python src/search_engine.py
```

---

## 🧪 Example Input

```
Enter target node: N100
```

---

## ✅ Example Output

```
Path: N1 -> N2 -> ... -> N100
Execution Time: 0.000045 seconds
```

---

## 📚 What I Learned

* How to convert CSV data into a graph structure
* How to optimize search using direct mapping
* How to improve performance using algorithms
* How to measure execution time in Python
* How to build a simple GUI application

---

## 👨‍💻 Author

**Austine**

---
