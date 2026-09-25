# CSV Search Engine

A high-performance CSV search engine that processes **5000+ nodes** using graph data structures and direct mapping optimization. Available as a Python desktop app **and** a live web app deployed on Vercel.

---

## Live Demo

Try it in your browser: **https://csv-search-engine.vercel.app**

No installation needed — the dataset loads in your browser and searches run instantly.

---

## How It Works

Instead of repeatedly scanning the dataset, the system converts CSV data into a **graph structure (adjacency list)** and builds a **direct mapping** of each node to its parent — enabling near-instant path retrieval.

### Algorithm & Approach

| Step | What happens | Complexity |
| --- | --- | --- |
| Preprocessing | CSV → adjacency list → direct parent map | O(n) |
| Search | Walk backward from target to root via parent map | ~O(1) |

- **Graph Representation** — adjacency list built from the CSV
- **Direct Mapping Optimization** — each node mapped directly to its parent (no repeated traversal)
- **Search Strategy** — parent-pointer walk inspired by BFS, but with O(1) per-step lookup

---

## Project Structure

```javascript
CSV_Search_Engine/
├── index.html          # Web version (Vercel)
├── style.css           # Web version styles
├── script.js           # Web version logic (same algorithm in JavaScript)
├── data/
│   └── data.csv        # Dataset: 5000+ node relationships
├── src/
│   ├── search_engine.py    # Terminal version
│   └── gui_app.py          # Desktop GUI version (tkinter)
├── generate_data.py    # Dataset generator script
└── README.md
```

---

## Usage

### Option 1: Web Version (no installation)

Visit the live demo, enter a start node (e.g. `N1`) and target node (e.g. `N100`), click **Search**.

### Option 2: Python Terminal Version

Requires Python 3.x (no external libraries needed).

```bash
git clone https://github.com/Austin-dev7/CSV_Search_Engine.git
cd CSV_Search_Engine
python src/search_engine.py
```

Menu options:

1. Search for a node (e.g. `N100`)
2. Run sample tests (N10, N50, N100)
3. Exit

### Option 3: Python GUI Version

```bash
python src/gui_app.py
```

A desktop window opens — enter a target node, click Search (or press Enter), and view the full path with execution time.

### Generating a New Dataset

```bash
python generate_data.py
```

This regenerates `data/data.csv` with fresh random node relationships.

---

## Example

**Input:** target node `N100`

**Output:**

```javascript
Path: N1 -> N2 -> N3 -> ... -> N100
Execution Time: 0.000045 seconds
```

---

## Tech Stack

- **Web version:** HTML, CSS, vanilla JavaScript
- **Desktop version:** Python 3 (csv, time, tkinter)
- **Deployment:** Vercel (static hosting)
- **Data:** CSV (Node, Neighbor pairs)

---

## What I Learned

- Converting CSV data into a graph structure (adjacency list)
- Optimizing search with direct parent mapping
- Measuring and comparing execution time
- Building a desktop GUI with tkinter
- Porting an algorithm from Python to JavaScript for the web

---

## Author

**Austine**