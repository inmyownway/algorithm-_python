n =int(input())

tree=[[] for _ in range(n)]

for i in range(n):
    n,m=map(int,input().split())
    tree[n].append(m)
    tree[m].append(n)

    #[ [] [2] [1,3,4] [2] [2] ]