# CSV Search Engine 🚀

## 📌 General Overview & Introduction (GOI)

This project is a high-performance CSV Search Engine built using Python. It is designed to efficiently process large datasets (5000+ nodes) by converting the data into a graph structure.

Instead of repeatedly scanning the dataset, the system applies an optimized **direct mapping technique**, enabling near-instant retrieval of paths between nodes.

The project demonstrates how proper use of **data structures and algorithm optimization** can significantly improve performance when working with large-scale data.

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
* User-friendly GUI interface (Tkinter)

---

## 🧠 Algorithm & Approach

This project combines multiple concepts:

* **Graph Representation**
  Data from the CSV file is converted into an adjacency list.

* **Direct Mapping Optimization**
  A dictionary is created to map each node directly to its parent, reducing search time.

* **Search Strategy**
  Inspired by Breadth-First Search (BFS), but optimized to avoid repeated traversal.

---

## ⚡ Performance

* **Preprocessing Time:** O(n)
* **Search Time:** ~ O(1) (near constant time)
* Extremely fast even with large datasets

---

## 🖥️ GUI Interface

The project includes a graphical user interface (GUI) built with Tkinter.

Users can:

* Enter a target node
* Click the search button
* View the full path in a scrollable display
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

## ▶️ How to Run

### 1. Generate Dataset

```
python generate_data.py
```

### 2. Run CLI Version

```
python src/search_engine.py
```

### 3. Run GUI Version

```
python src/gui_app.py
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
* Difference between normal search and optimized search
* How to measure execution time in Python
* How to build a GUI application using Tkinter

---

## 👨‍💻 Author

**Austine**

---
