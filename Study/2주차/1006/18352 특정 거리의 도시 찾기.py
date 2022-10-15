from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        d = q.popleft()
        for i in graph[d]:
            print(graph[d])
            if graph[i] == False:
                graph[i] = True
                result[i]=result[d]+1

                q.append(i)

n,m,k,start=map(int,input().split())
graph = [ [] for _ in range(n+1)]
visited = [False for i in range(n+1)]
result = [ 0 for _ in range(n+1)]

for i in range (m):
    x, y = map(int,input().split())
    graph[x].append(y)
print(graph)



bfs(start)

print(result)


