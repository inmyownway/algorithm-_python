
n = int(input())
home = list(map(int,input().split()))

home.sort()


# 1 5 7 9
sum=0
min = 999999999
for i in range(len(home)):
    for j in range(len(home)):
        if i == j:
            continue
        else:
            sum += abs(home[j]-home[i])

    if min > sum:
        min = sum
        num = i
    sum =0


print(home[num])



