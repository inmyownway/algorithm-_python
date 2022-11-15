T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    game=[]
    for i in range(n):
        t =list(input())
        game.append(t)
    print(game)
    for i in range(n):
        for j in range(m):
            if game[i][j]== '>' or game[i][j]== '<' \
                    or game[i][j]== '^' or game[i][j]== 'v':
                 current= game[i][j]

                 y = i
                 x = j
                 print(y,x,current)
                 break
    len_inp=int(input())
    inp = list(input()) # (2,1) -> (1,1)
    print(inp)
    for i in inp:
        print(x,y)
        if i == 'U' and y-1 >=0:
            if game[x][y-1] == ".":
                current = "^"
                game[x][y]= '.'
                game[x][y-1]= '^'
                y-=1
        elif i == 'D' and y+1 <=n-1:
            if game[x][y+1] == ".":
                curent="v"
                game[x][y] = '.'
                game[x][y + 1] = "v"
            y+=1
        elif i == 'L' and x -1 >=0:
            if   game[x-1][y] == ".":
                curent = "<"
                game[x][y] = '.'
                game[x-1][y] = "<"
                x-= 1
        elif i == 'R' and x + 1 < m-1:
            if game[y][x+1] == ".":
                curent = ">"
                game[y][x] = '.'
                game[y][x+1] = ">"
                x += 1
        elif i == 'S':
            #print(current)
            if current == '^':
                for j in range(y-1,-1,-1):
                    if game[x][j] == '*':
                        game[x][j] = '.'
                        break
                    elif game[x][j] == '#':
                        break
            if current == 'v':
                for j in range(y+1,n):
                    if game[x][j] == '*':
                        game[x][j] = '.'
                        break
                    elif game[x][j] == '#':
                        break
            if current == '<':
                for j in range(x-1,-1,-1):
                    if game[j][y] == '*':
                        game[j][y] = '.'
                        break
                    elif game[j][y] == '#':
                        break
            if current == '>':
                for j in range(x+1,m):
                    if game[j][y] == '*':
                        game[j][y] = '.'
                        break
                    elif game[j][y] == '#':
                        break

    print(game)






