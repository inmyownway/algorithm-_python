
t= int(input())
for i in range (t):
    a,b=map(int,input().split())

    n=list(map(int,input().split()))
    m=list(map(int,input().split()))


    n.sort()
    m.sort()
    count=0

    for i in n:
        for j in m:
            if i > j:
                count+=1
    print(count)