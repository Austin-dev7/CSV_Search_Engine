import tkinter as tk
from tkinter import messagebox
import time
from search_engine import build_graph, build_direct_map, ultra_fast_search

# Load data
graph = build_graph("data/data.csv")
direct_map = build_direct_map(graph)

# ================= FUNCTIONS =================

def run_search():
    target = entry.get().strip()

    # Validation
    if target == "":
        messagebox.showwarning("Input Error", "Please enter a target node")
        return

    if target not in graph and target not in direct_map:
        result_label.config(text="Node not found in dataset", fg="red")
        time_label.config(text="")
        return

    start_time = time.time()
    result = ultra_fast_search(direct_map, target)
    end_time = time.time()

    if result:
        path = " -> ".join(result)
        result_label.config(text=f"Path:\n{path}", fg="green")
    else:
        result_label.config(text="No path found", fg="red")

    time_label.config(text=f"Execution Time: {end_time - start_time:.6f} seconds")


def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")
    time_label.config(text="")

# ================= GUI SETUP =================

root = tk.Tk()
root.title("CSV Search Engine")
root.geometry("650x420")
root.resizable(False, False)

# Center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (650 // 2)
y = (screen_height // 2) - (420 // 2)
root.geometry(f"650x420+{x}+{y}")

# ================= UI ELEMENTS =================

# Title
title = tk.Label(root, text="CSV Search Engine", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Input section
frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter Target Node:", font=("Arial", 12))
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=25, font=("Arial", 12))
entry.grid(row=0, column=1, padx=5)
entry.focus()  # Auto-focus

# Allow Enter key to trigger search
root.bind('<Return>', lambda event: run_search())

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

search_btn = tk.Button(button_frame, text="Search", width=12, command=run_search)
search_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", width=12, command=clear_fields)
clear_btn.grid(row=0, column=1, padx=10)

# Result section
result_title = tk.Label(root, text="Result", font=("Arial", 12, "bold"))
result_title.pack()

result_label = tk.Label(root, text="", wraplength=550, justify="center", font=("Arial", 11))
result_label.pack(pady=10)

# Execution time section
time_title = tk.Label(root, text="Execution Details", font=("Arial", 12, "bold"))
time_title.pack()

time_label = tk.Label(root, text="", font=("Arial", 10))
time_label.pack()

# Run app
root.mainloop()