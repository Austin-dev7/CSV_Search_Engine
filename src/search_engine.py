import csv
import time

# ================= GRAPH CREATION =================

# This function reads a CSV file and converts it into a graph (dictionary)
def build_graph(file_path):
    graph = {}  # stores nodes and their connections

    # Open the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        # Loop through each row in the CSV
        for row in reader:
            node = row["Node"]        # starting node
            neighbor = row["Neighbor"]  # connected node

            # If node not already in graph, create it
            if node not in graph:
                graph[node] = []

            # Add neighbor to the node's list
            graph[node].append(neighbor)

    return graph


# ================= OPTIMIZATION =================

# This function creates a "direct map" for faster searching
# Instead of searching through the whole graph,
# we directly map each node to its parent
def build_direct_map(graph):
    direct_map = {}

    # Loop through each node and its neighbors
    for start in graph:
        for neighbor in graph[start]:
            # Store parent of each neighbor
            direct_map[neighbor] = start

    return direct_map


# ================= SEARCH ALGORITHM =================

# Ultra fast search using direct mapping
# This avoids BFS and makes search much faster
def ultra_fast_search(direct_map, target):
    path = []

    # Move backward from target to the root node
    while target in direct_map:
        path.append(target)              # add current node to path
        target = direct_map[target]      # move to parent node

    # Add the starting node
    path.append(target)

    # Reverse to get correct order (start → target)
    path.reverse()

    return path


# ================= MAIN PROGRAM =================
def show_menu():
    print("\n" + "="*40)
    print("      CSV SEARCH ENGINE (GOI)")
    print("="*40)
    print("1. Search for a node")
    print("2. Run sample test")
    print("3. Exit")
    print("="*40)


def run_system(graph, direct_map):
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            target = input("\nEnter target node: ")

            if target not in graph and target not in direct_map:
                print("\n❌ Node does not exist in dataset")
                continue

            start_time = time.time()
            result = ultra_fast_search(direct_map, target)
            end_time = time.time()

            print("\n✅ Result:")
            print("Path:", " -> ".join(result))
            print(f"⏱ Time: {end_time - start_time:.6f} seconds")

        elif choice == "2":
            print("\nRunning sample tests...")
            samples = ["N10", "N50", "N100"]

            for target in samples:
                result = ultra_fast_search(direct_map, target)
                print(f"\nTarget: {target}")
                print("Path:", " -> ".join(result))

        elif choice == "3":
            print("\n👋 Exiting system...")
            break

        else:
            print("\n❌ Invalid choice")


# ================= RUN =================
graph = build_graph("data/data.csv")
direct_map = build_direct_map(graph)

run_system(graph, direct_map)