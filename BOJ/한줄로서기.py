
n=int(input())
m=list(input().split())

ans=[0]*n
# 2 1 1 0

# 4 2 1 3
for i in range(1,n+1):
    temp = n[i-1]
    cnt = 0
    for j in range(n):
        if cnt==temp and ans[j]==0:
            ans[j]=temp
            break
        elif ans[j]==0:
            cnt+=1
