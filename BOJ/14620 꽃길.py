from itertools import combinations
n=int(input())

price=[]
answer= int(1e9)
for i in range(n):
    temp=list(map(int,input().split()))
    price.append(temp)

def check(li):
    global answer
    m=[[0]* n for _ in range(n)]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for x,y in li:

        #print(x,y)
        m[x][y]=1
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if m[nx][ny]==0:
                m[nx][ny]=1
            elif m[nx][ny]:
                #print(x,y)
                return
    #print("ASdsadas")
    result =0
    for i in range(n):
        for j in range(n):
            if m[i][j]==1:
                result+=price[i][j]
   #print(result)
    answer=min(answer,result)




can = [(r,c) for r in range(1,n-1) for c in range(1,n-1)]
candidates=list(combinations(can,3))

for candidate in candidates:
    check(candidate)
print(answer)