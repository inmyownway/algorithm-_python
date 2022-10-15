from collections import deque

dx= [0,0,1,-1]
dy= [1,-1,0,0]

def bfs(graph, i ,j):
    n = len(graph)
    q = deque()
    q.append((i,j))
    graph[i][j] = 0
    count = 1

    while q:
        x,y =q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny]=0
                q.append((nx, ny))
                count+=1
    return count


n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))


cnt =[]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            c = bfs(graph, i, j)
            cnt.append(c)
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
