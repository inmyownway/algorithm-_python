
n=int(input())
x,y=1,1
nx = [0,0,-1,1]
ny = [1,-1,0,0]

s =list(input().split())

for i in s:
    if i == 'U':
        x+=nx[0]
        y+=ny[0]
    if i == 'D':
        x+=nx[1]
        y+=ny[1]
    if i == 'R':
        x+=nx[3]
        y+=ny[3]
    if i == 'L':
        x+=nx[2]
        y+=ny[2]
print(x,y)
