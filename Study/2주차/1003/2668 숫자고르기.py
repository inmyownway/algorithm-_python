n = int(input())
graph = [0] + [int(input()) for _ in range(n)]
visited = [False]*(n+1)


for i in range(1,n+1):
    temp =set()
    start = i
    if not visited[start]:
        while True:
            next = graph[start]
            if next not in temp:
                temp.add(next)
                start = next
                if next == i:
                    for t in temp:
                        visited[t]=True
                    break
            else:
                break

print(visited.count(True))
for i in range(1,n+1):
    if visited[i]==True:
        print(i)