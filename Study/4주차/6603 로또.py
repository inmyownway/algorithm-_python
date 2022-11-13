import itertools
from itertools import combinations

while True:
    l=list(map(int,input().split()))
    if l[0]==0:
        break
    #num = l[0]
    li =l[1:]
    for i in itertools.combinations(li,6):
        # i = (1,2,3,4,5,6)
        for j in range(len(i)):
            print(i[j],end=' ')
        print()
    print()


