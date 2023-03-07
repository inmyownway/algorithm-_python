
n= int(input())
k = int(input())
data=[[0]*(n+1) for _ in range (n+1)]
info=[]

for i in range(k):
    a,b=map(int,input().split())
    data[a][b]==1

l=int(input())
for i in range(l):
    x,c=input().split()
    info.append((int(x)),c)
# 동 남 서 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,c):
    if c=="L":
        direction = (direction-1)%4
    else:
        direction=(direction+1)%4

def simulate():
    x,y=1,1
    data[1][1]=2
    direction = 0 # 처음에는 동쪽 바라봄
    time = 0
    index= 0
    d=[(x,y)]
    while True:
