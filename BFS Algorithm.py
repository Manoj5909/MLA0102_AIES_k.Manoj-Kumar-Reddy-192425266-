from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)
    print("\nBFS Traversal:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
n = int(input("Enter number of vertices: "))
graph = {}
print("\nEnter the vertex names:")
for i in range(n):
    vertex = input(f"Vertex {i+1}: ")
    graph[vertex] = []
e = int(input("\nEnter number of edges: "))
print("\nEnter edges (Source Destination):")
for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    graph[u].append(v)
    graph[v].append(u)
start = input("\nEnter starting vertex: ")
bfs(graph, start)
