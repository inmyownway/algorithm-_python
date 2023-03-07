from collections import deque
n,k=map(int,input().split())
graph=[]
data=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))
            # 바이러스 종류,시간 , 위치

data.sort()
q=deque(data)

target_s,target_x,target_y = map(int,input().split())

dx=[-1,0,1,0]
dy=[0,1,0,-1]

while q:
    virus,s,x,y = q.popleft()
    if s== target_s:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus,s+1,nx,ny))
print(graph[target_x-1][target_y-1])




#
# virus=[]
# ts = [[] for _ in range(k)]
# for i in range(n):
#     temp=list(map(int,input().split()))
#     for j in range(n):
#         if temp[j]!=0:
#             ts[temp[j]-1].append((i,j))
#     virus.append(temp)
# #print(ts)
# s,wx,wy=map(int,input().split())
# #print(virus)
# count = 0
#
# order =1
# while count<s:
#     count+=1
#
#     dx=[0,0,-1,1]
#     dy=[1,-1,0,0]
#     q=deque()
#
#     #print(ts)
#     #check = [[False] * n for _ in range(n)]
#     # for a in range(1,k+1):
#     #     for i in range(n):
#     #         for j in range(n):
#     #             if virus[i][j]==a:
#     #                 ts[a-1].append((i,j))
#     # [ [0,0],[2,1],[3] ]
#     for t in ts:
#         for i in t:
#             x,y=i
#             #check[x][y]=True
#             for j in range(4):
#                 nx =x+dx[j]
#                 ny= y+dy[j]
#                 if 0<= nx < n and 0<= ny <n and virus[nx][ny]==0:
#                     virus[nx][ny]=virus[x][y]
# #print(virus)
# print(virus[wx-1][wy-1])



