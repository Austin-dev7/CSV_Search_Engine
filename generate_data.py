import csv

with open("data/data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Node", "Neighbor"])

    # Create a chain: A1 → A2 → A3 → ... → A5000
    for i in range(1, 5000):
        node = f"N{i}"
        neighbor = f"N{i+1}"
        writer.writerow([node, neighbor])

print("✅ Connected dataset (5000 nodes) created")