from collections import deque


for test_case in range(1, 11):
    T=int(input())
    l=list(map(int,input().split()))
    l=deque(l)
    cycle_count=1
    while True:
        if cycle_count == 6:
            cycle_count=1
        front = l.popleft()
        if front - cycle_count > 0:
            l.append(front-cycle_count)
        else:
            l.append(0)
            break
        cycle_count+=1
    l=list(l)
    print("#%d %d %d %d %d %d %d %d %d" %(test_case,l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7]))

