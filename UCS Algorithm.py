import heapq
def ucs(graph,start,goal):
    pq=[]
    heapq.heappush(pq,(0,start))
    visited={}
    parent={}
    while pq:
        cost,node=heapq.heappop(pq)
        if node in visited:
            continue
        visited[node]=cost
        if node==goal:
            path=[]
            current=goal
            while current!=start:
                path.append(current)
                current=parent[current]
            path.append(start)
            path.reverse()
            print("\nMinimum Cost Path:")
            print(" -> ".join(path))
            print("Minimum Cost:",cost)
            return
        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq,(cost+weight,neighbor))
                if neighbor not in parent:
                    parent[neighbor]=node
    print("Goal node not reachable.")
n=int(input("Enter number of vertices: "))
graph={}
print("\nEnter the vertex names:")
for i in range(n):
    vertex=input(f"Vertex {i+1}: ")
    graph[vertex]=[]
e=int(input("\nEnter number of edges: "))
print("\nEnter edges (Source Destination Cost):")
for i in range(e):
    u,v,w=input(f"Edge {i+1}: ").split()
    w=int(w)
    graph[u].append((v,w))
    graph[v].append((u,w))
start=input("\nEnter starting vertex: ")
goal=input("Enter goal vertex: ")
ucs(graph,start,goal)
