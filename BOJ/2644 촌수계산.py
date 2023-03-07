from collections import deque
n=int(input())
family=[[] for _ in range(n+1)]
visited=[False] * (n+1)
answer = -1

x,y=map(int,input().split())

m=int(input())
for i in range(m):
    tx,ty=map(int,input().split())
    family[tx].append(ty)
    family[ty].append(tx)
# 1 - 2
# 2 - 3
# [2] [1,3] [3]
# True
def bfs(x):
    global answer
    q=deque([(x,0)])
    # q= [(1,0)] ,[2,1]
    while q:
        node,cnt = q.popleft()

        if node == y:
            answer = cnt

        for i in family[node]:
            if visited[i]==False:
                visited[i]=True
                q.append([i,cnt+1])

bfs(x)
print(answer)