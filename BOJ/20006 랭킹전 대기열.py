
p,m=map(int,input().split())
rooms=[]

for p in range(p):
    level,name = input().split()

    if not rooms:
        rooms.append([[int(level),name]])
        continue
    # rooms = [ [[1,p]] ]
    enter=False
    for room in rooms:
        if len(room)< m and room[0][0]-10 <= int(level)<=room[0][0]+10:
            room.append([int(level),name])
            enter=True
            break
    if not enter:
        rooms.append([[int(level),name]])

for room in rooms:
    room.sort(key=lambda x:x[1])

for room in rooms:
    if len(room)==m:
        print("Started!")
    else:
        print("Waiting!")
    for l,n in room:
        print(l,n)