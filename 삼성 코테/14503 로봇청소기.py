from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 서 북
n, m = map(int, input().split())
r, c, d = map(int, input().split())
visited = [[0] * m for _ in range(n)]
# d
# 0 북
# 1 동
# 2 남
# 3 서
graph = []
for i in range(n):
    t = list(map(int, input().split()))
    graph.append(t)

visited[r][c] = True
count = 1
while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(count)
            break
        else:
            r,c = r-dx[d],c-dy[d]












