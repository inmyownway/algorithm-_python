from collections import deque
k=int(input())
n,m=map(int,input())

graph=[]

for i in range(n):
    temp=list(map(int,input().split()))

horse_mov=[[-1,-2],[-1,2],[-2,-1],[-2,1],
           [1,-2],[1,2],[2,-1],[2,1]]

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def bfs():
    visited=[[]]
q=deque()

