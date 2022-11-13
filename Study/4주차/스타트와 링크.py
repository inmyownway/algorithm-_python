import itertools
import sys
from itertools import permutations
n = int(input())
temp =[]
for i in range (n):
    temp.append(i)
graph = []
for i in range (n):
    t = list(map(int,input().split()))
    graph.append(t)
nums=[]
for i in range (n):
    nums.append(i)

teams = list(itertools.combinations(nums,len(nums)//2))
#print(teams)
min =  sys.maxsize

for team in teams:
    t1 = 0
    t2 = 0

    for i in  team:
        for j in  team:
            t1+=graph[i][j]

    not_team = [x for x in range(n) if x not in team]

    for i in not_team:
        for j in not_team:
            t2+=graph[i][j]

    if min > abs(t1-t2):
        min = abs(t1-t2)
print(min)