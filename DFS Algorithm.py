def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
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
visited = set()
print("\nDFS Traversal:")
dfs(graph, start, visited)
