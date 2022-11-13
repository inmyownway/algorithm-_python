n = int(input())

tree =list(map(int,input().split()))

l = [[] for _ in range (n)]

# 1 6 4
# 3
# 5 2 7

def dfs(tree,depth):

    mid = (len(tree)//2)
    l[depth].append(tree[mid])

    if len(tree)==1:
        return
    dfs(tree[:mid],depth+1)
    dfs(tree[mid+1:],depth+1)

dfs(tree,0)

for i in l:
    print(*i)