from collections import deque

n = int(input())
family = [[] for _ in range(n+1)]
result = [0 for i in range(n+1)]
x,y=map(int,input().split())
num = int(input())

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for i in range(n + 1)]
    visit[start] = 1
    while q:
        d = q.popleft()
        for i in family[d]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[d] + 1
                q.append(i)
        print(result)

for i in range(0,num):
    a,b=map(int,input().split())
    family[a].append(b)
    family[b].append(a)
bfs(x)
if(result[y]==0):
    print(-1)
else:
    print(result[y])