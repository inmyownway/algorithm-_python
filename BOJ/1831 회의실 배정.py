n=int(input())

time=[]
for i in range(n):
    n,m=map(int,input().split())
    time.append([n,m])

time = sorted(time, key = lambda a : a[0]) # start 기준으로 오름차순 정렬
print(time)
time = sorted(time, key = lambda a : a[1]) #
print(time)
count =0