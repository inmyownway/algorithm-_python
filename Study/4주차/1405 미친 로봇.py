
#단순한 경우는 같은곳을 한번보다 많이 이동하지 않을때
import itertools
n, e, w, s, n = map(int,input())
group =['e','w','s','h']
route = list(itertools.permutations(group,n))
p=1
for i in route:
    for i in len(route)
