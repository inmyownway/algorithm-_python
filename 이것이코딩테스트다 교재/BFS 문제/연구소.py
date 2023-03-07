from collections import deque
from sys import stdin
import copy
input = stdin.readline

n,m=map(int,input().split())

map1=[]
for i in range(n):
    t=list(map(int,input().split()))
    map1.append(t)

dx=[-1,1,0,0]
dy=[0,0,1,-1]

answer=0


def get_score(map2):
    score=0
    for i in range(n):
        for j in range(m):
            if map2[i][j]==0:
                score+=1
    return score

def bfs():
    global answer
    q = deque()
    map2 = copy.deepcopy(map1) # 2차원 배열을 복사하는 부분

    """ 바이러스가 있는 지점에서 시작한다. 
    동시에 유포해야 하니깐 이렇게 미리 바이러스 지점을 큐에 집어넣는다."""
    for i in range(n):
        for j in range(m):
            if map2[i][j] == 2:
                q.append((i, j))

    while q:
        px, py = q.popleft()

        for k in range(4):
            mx = px + dx[k]
            my = py + dy[k]
            if 0 <= mx < n and 0 <= my < m:
                if map2[mx][my] == 0:
                    map2[mx][my] = 2
                    q.append((mx, my))

    global answer
    # cnt = 0
    # for i in range(n):
    #     cnt += map2[i].count(0)

    answer = max(answer,get_score(map2) )

def wall(cnt): # 백트래킹 부분. 벽이 3개 다 세워지면 bfs를 탐색한다.
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if map1[i][j] == 0:
                map1[i][j] = 1
                wall(cnt+1)
                map1[i][j] = 0
wall(0)
print(answer)




