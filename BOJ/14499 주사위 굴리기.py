n,m,x,y,c_num=map(int,input().split())

jido=[]
for i in range(n):
    temp=list(map(int,input().split()))
    jido.append(temp)

c=list(map(int,input().split()))

# def rolling(i,dice,f):
#
#     if i==1:
#         new=[dice[5],dice[1],dice[4],dice[3],dice[0],dice[2]]
#
#
#     return new
#

dice=[0, 0, 0, 0 ,0 , 0]
#    아래,북, 위,남, 동  서
# 3 북쪽
# 아래 -> 남
# 북 ->  아래
# 위 ->  북
# 남 -> 위
# 동 ->  동
# 서 ->서

# dice=[dice[4],dice[1],dice[5],dice[3],dice[2],dice[0]]

for i in c:

    if i==1 and y+1<m :
        #print(i,"i")
        dice=[dice[5],dice[1],dice[4],dice[3],dice[0],dice[2]]
        r=jido[x][y+1]

        if r==0:

            jido[x][y+1]=dice[0]
        elif r!=0:

            dice[0]=r
            jido[x][y+1]=0
        print(dice[2])
        y += 1
    if i==2 and y-1>=0:

        #print(i, "i")
        dice=[dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]]
        r=jido[x][y-1]

        if r == 0:
            jido[x][y- 1] = dice[0]
        elif r != 0:
            dice[0] = r
            jido[x][y - 1] = 0
        print(dice[2])
        y-=1
    if i==3 and x-1>=0:

        #print(i, "i")
    #    dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
        dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]

        r = jido[x-1][y]

        if r == 0:
            jido[x-1][y] = dice[0]
        elif r != 0:
            dice[0] = r
            jido[x-1][y] = 0
        x -= 1
        print(dice[2])

    if i==4 and x+1<n:

        #print(i, "i")
        dice =[dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]
        r = jido[x + 1][y]

        if r == 0:
            jido[x +1][y] = dice[0]
        elif r != 0:
            dice[0] = r
            jido[x + 1][y] = 0
        x+=1
        print(dice[2])







