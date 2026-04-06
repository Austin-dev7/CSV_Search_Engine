import csv
import time

# Build graph from CSV
def build_graph(file_path):
    graph = {}

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            node = row["Node"]
            neighbor = row["Neighbor"]

            if node not in graph:
                graph[node] = []

            graph[node].append(neighbor)

    return graph


# Build direct map (for fast search)
def build_direct_map(graph):
    direct_map = {}

    for start in graph:
        for neighbor in graph[start]:
            direct_map[neighbor] = start

    return direct_map


# Ultra fast search
def ultra_fast_search(direct_map, target):
    path = []

    while target in direct_map:
        path.append(target)
        target = direct_map[target]

    path.append(target)
    path.reverse()

    return path


# ================= MAIN =================

graph = build_graph("data/data.csv")
direct_map = build_direct_map(graph)

target = input("Enter target node: ")

# Validation
if target not in graph and target not in direct_map:
    print("\n❌ Node does not exist in dataset")
    exit()

start_time = time.time()

result = ultra_fast_search(direct_map, target)

end_time = time.time()

if result:
    print("\n✅ Result:")
    print("Path:", " -> ".join(result))
else:
    print("\n❌ Result: No path found")

print(f"\n⏱ Execution Time: {end_time - start_time:.6f} seconds")