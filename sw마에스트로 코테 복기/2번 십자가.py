
lines=[[0,3,3,3],[1,0,1,2],[1,0,5,0],[4,0,4,3],[2,1,2,3]]

lines=[[1,3,5,3],[3,1,3,5]]

max_line =-1
for line in lines:
    #print(line)
    for l in line:
        if l > max_line:
            max_line=l
#print(max_line)

graph=[[0]*(2*max_line) for _ in range(max_line*2)]
z=1
for line in lines:
    x1,y1,x2,y2=line[0]*2,line[1]*2,line[2]*2,line[3]*2

    if y1==y2:
        for i in range(x1,x2):
            graph[y2][i]=z
    elif x1==x2:
        for i in range(y1,y2):
            graph[i][x1]=z
    z+=1

for i in graph:
    print(i)