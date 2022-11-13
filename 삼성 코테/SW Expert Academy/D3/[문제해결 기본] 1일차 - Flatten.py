T = 10
for test_case in range(1, T + 1):
    n=int(input())
    count=0
    l=list(map(int,input().split()))
    while True:

        l.sort()
        if count == n or l[-1] - l[0] == 1:
            print("#%d %d" %(test_case,l[-1]-l[0]))
            break

        l[-1]-=1
        l[0]+=1
        count+=1



