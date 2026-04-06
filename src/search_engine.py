import csv
import time
from collections import deque


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

def build_direct_map(graph):
    direct_map = {}

    for start in graph:
        for neighbor in graph[start]:
            direct_map[neighbor] = start

    return direct_map

def build_reverse_index(graph):
    reverse_index = {}

    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in reverse_index:
                reverse_index[neighbor] = []

            reverse_index[neighbor].append(node)

    return reverse_index

def fast_search(graph, reverse_index, target):
    # If target is a starting node
    if target in graph:
        return [target]

    # If target exists in reverse index
    if target not in reverse_index:
        return None

    start = reverse_index[target][0]

    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

    # pick first parent
    start = reverse_index[target][0]

    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

# MAIN PROGRAM
graph = build_graph("data/data.csv")
reverse_index = build_reverse_index(graph)

print("Graph:", graph)

target = input("Enter target node: ")

# ✅ Safe validation (add this)
if target not in graph and target not in direct_map:
    print("\n❌ Node does not exist in dataset")
    exit()

start_time = time.time()

result = fast_search(graph, reverse_index, target)

end_time = time.time()

if result:
    print("\n✅ Result:")
    print("Path:", " -> ".join(result))
else:
    print("\n❌ Result: No path found")

print(f"\n⏱ Execution Time: {end_time - start_time:.6f} seconds")