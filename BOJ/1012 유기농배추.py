from collections import deque
test_case = int(input())
for test in range(test_case):
    m,n,pos = list(map(int,input().split()))

    l=[[0]*m for _ in range(n)]
    #print(l)
    for i in range(pos):
        x,y=map(int,input().split())
        #print(x,y)
        l[y][x]=1

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    #  가로길이 M  세로길이 N
    q=deque()
    #print(l)
    visited=[[False] * m for _ in range(n)]
    cnt=0
    #print(visited)
    for a in range(n):
        for b in range(m):
            if visited[a][b]==False and l[a][b]==1:

                cnt+=1
                #print("!",cnt)
                q.append((a,b))
                while q:

                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False \
                                and l[nx][ny]==1:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                #print(visited)

    print(cnt)


