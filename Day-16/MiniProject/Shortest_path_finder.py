from collections import deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


# Example Graph
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

start = "A"
end = "F"
print(f"Shortest Path from {start} to {end}: ", shortest_path(graph, start, end))
