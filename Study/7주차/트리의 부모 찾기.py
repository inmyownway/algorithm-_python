from collections import deque

n=int(input())
visited = [False]*(n+1)
answer = [0] *(n+1)

matrix = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    matrix[a].append(b)
    matrix[b].append(a)

def bfs(matrix,node,visited):
    q =deque([node])
    visited[node]=True

    while q:
        temp = q.popleft()
        for i in matrix[temp]:
            if visited[i] == False:
                answer[i]=temp
                visited[i]=True
                q.append(i)

bfs(matrix,1,visited)

for i in range(2,n+1):
    print(answer[i])