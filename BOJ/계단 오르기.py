import sys
n=int(input())
staris=[]

for i in range(n):
    staris.append(int(input()))

dp=[0]*(n+1)

dp[0]=staris[0]

if n==1:
    print(dp[0])
    sys.exit(0)
dp[1]=staris[0]+staris[1]
if n==2:
    print(dp[1])
    sys.exit(0)

dp[2]=max(staris[0]+staris[2],staris[1]+staris[2])
# [10,20,15,25,10,20]

for i in range(3,n):
    dp[i]=max(dp[i-2]+staris[i],dp[i-3]+staris[i-1]+staris[i])



