from collections import deque
n, m, v = map(int,input().split())
group=[[] for _ in range(n+1)]

for i in range(m):
    a,b= map(int,input().split())
    group[a].append(b)
    group[b].append(a)



print(group)

def bfs(start):
    check = [0] * (n+1)
    q= deque()
    q.append(start)
    check[start]=1
    while q:
        x =q.popleft()
        print(x, end=' ')
        for y in group[x]:
            if check[y] == 0:
                check[y] = 1
                q.append(y)
def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)
bfs(v)
4 5 1
1 2
1 3
1 4
2 4
3 4
