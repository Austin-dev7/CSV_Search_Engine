import tkinter as tk
from tkinter import scrolledtext
import time
from search_engine import build_graph, build_direct_map, ultra_fast_search

# Load data
graph = build_graph("data/data.csv")
direct_map = build_direct_map(graph)

# Function to handle search
def search():
    target = entry.get()
    
    if target not in graph and target not in direct_map:
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, "❌ Node not found")
        return

    start = time.time()
    path = ultra_fast_search(direct_map, target)
    end = time.time()

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, " -> ".join(path))

    time_label.config(text=f"⏱ Time: {end - start:.6f} seconds")

# Create window
root = tk.Tk()
root.title("CSV Search Engine")
root.geometry("700x500")
root.configure(bg="#1e1e1e")  # dark background

# Title
title = tk.Label(root, text="CSV Search Engine", font=("Arial", 20, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=10)

# Input
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

# Button
search_btn = tk.Button(root, text="Search", font=("Arial", 12), bg="#4CAF50", fg="white", command=search)
search_btn.pack(pady=5)

# Result box (SCROLLABLE)
result_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15, font=("Arial", 10))
result_box.pack(pady=10)

# Time label
time_label = tk.Label(root, text="⏱ Time: ", font=("Arial", 12), fg="white", bg="#1e1e1e")
time_label.pack()

# Run app
root.mainloop()