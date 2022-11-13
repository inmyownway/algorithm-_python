from collections import deque

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    q=deque()
    graph=[]
    visited= [ [0] * w for _ in range(h)]
    count =0
    #print(visited)
    for i in range (h):
        temp= list(map(int,input().split()))
        graph.append(temp)
    #print(graph)
    x=[0,0,-1,1,-1,1,-1,1]
    y=[1,-1,0,0,1,1,-1,-1]


    for i in range (h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==0:
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    current_x,current_y = q.popleft()
                    #print("cx cy",current_x,current_y)
                    for a in range(8):
                        dx = current_x + x[a]
                        dy = current_y + y[a]
                        if dx >= 0 and dx < h and dy >=0 and dy<w:
                            #print("@@",dx," ",dy)
                            #print(i,j)
                            t = graph[dx][dy]
                            if t == 1 and visited[dx][dy] == 0:
                                q.append((dx,dy))
                                visited[current_x+x[a]][current_y+y[a]]=1
                        else:
                            continue
                        dx = 0
                        dy = 0
                count+=1

    print(count)


