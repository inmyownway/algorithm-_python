import itertools
from itertools import permutations
n = int(input())
temp =[]
for i in range (n):
    temp.append(i)

graph = []

for i in range (n):
    t = list(map(int,input().split()))
    graph.append(t)

w = list(itertools.permutations(temp))
print(w)
min=9999999
sum=0
for i in w:
    for j in range (len(i)-1):
        if graph[i[j]][i[j+1]] == 0:
            continue
        sum += graph[i[j]][i[j+1]]
        sum += graph[i[len(i)-1]][i[0]]
    if min > sum:
        a=i
        min = sum

    sum=0
print(a,min)

