from collections import deque
n, m, v = map(int,input().split())
group=[[] for _ in range(n+1)]

for i in range(m):
    a,b= map(int,input().split())
    group[a].append(b)
    group[b].append(a)

visited=[0]* (n+1)

print(group)

def bfs(group,visited,start):
    q= deque()
    q.append(start)
    visited[start]=1
    while q:
        current =q.popleft()
        print(current,end=' ')
        for i in group[current]:
            if visited[i] == 0:
                visited[i] ==1
                q.append(i)

#bfs(group,visited,v)
