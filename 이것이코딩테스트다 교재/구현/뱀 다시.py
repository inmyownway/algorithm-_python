from collections import deque
n=int(input())
apple =int(input())


m = [[0]*n for _ in range(n)]
for i in range(apple):
    x,y=map(int,input().split())
    m[x-1][y-1]=2

control=[]
move =int(input())
for i in range(move):
    x,y=input().split()
    control.append([int(x),y])
x=0
y=0
m[x][y]=1
ci=0
snake = deque()
snake.append((0,0))
state= 'R'
second = 0
# 0 1 2 3
# 동 남 서 북
g = ['R','D','L','U']

index =0
while True:
    second+=1

    if state=='R':
        if y+1>=n:
            break
        if m[x][y + 1] == 1:
            break
        # 아무것도 없음 -> 꼬리 한칸 줄임
        elif m[x][y+1]== 0:
            snake.append((x,y+1))
            tx,ty=snake.popleft()
            m[tx][ty]=0
            m[x][y+1]=1
            y+=1
        # 사과발견 몸길이 추가
        elif m[x][y+1]==2:
            snake.append((x, y + 1))
            m[x][y+1]=1
            y+=1
    if state=='L':
        if y-1<0:
            break
        elif m[x][y - 1] == 1:
            break
        # 아무것도 없음 -> 꼬리 한칸 줄임
        elif m[x][y-1]== 0:
            snake.append((x,y-1))
            tx,ty=snake.popleft()
            m[tx][ty]=0
            m[x][y-1]=1
            y-=1
        # 사과발견 몸길이 추가
        elif m[x][y-1]==2:
            snake.append((x, y - 1))
            m[x][y-1]=1
            y-=1
    if state=='U':
        if x-1<0:
            break
        elif m[x-1][y] == 1:
            break
        # 아무것도 없음 -> 꼬리 한칸 줄임
        elif m[x-1][y]== 0:
            snake.append((x-1,y))
            tx,ty=snake.popleft()
            m[tx][ty]=0
            m[x-1][y]=1
            x-=1
        # 사과발견 몸길이 추가
        elif m[x-1][y]==2:
            snake.append((x - 1, y))
            m[x-1][y]=1
            x -= 1

    if state=='D':

        if x+1 >=n:
            break
        if m[x+1][y] == 1:
            break
        # 아무것도 없음 -> 꼬리 한칸 줄임
        elif m[x+1][y]== 0:
            snake.append(((x+1,y)))
            tx,ty=snake.popleft()
            m[tx][ty]=0
            m[x+1][y]=1
            x+=1
        # 사과발견 몸길이 추가
        elif m[x+1][y]==2:
            snake.append(((x+1, y )))
            m[x+1][y]=1
            x +=1
    if len(control)!=0:
        if second == control[ci][0]:
            new_state=control[ci][1]
            if new_state =="L":
                index= (index-1)%4
            else:
                index= (index+1)%4
            #print(index)
            state = g[index]
            if ci < len(control)-1:
                ci+=1



    # for i in range(n):
    #     for j in range(n):
    #         print(m[i][j],end="")
    #     print()
    # print()
print(second,end="")







