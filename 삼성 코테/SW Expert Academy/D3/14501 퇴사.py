n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    sum = 0
    for j in l:
        if j % 2 == 1:
            sum += j
    print("#%d %d" % (i+1,sum))