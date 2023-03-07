def change(num):
    if switch[num]==0:
        switch[num]=1
    else:
        switch[num]=0
    return
n = int(input())

switch = [-1]+ list(map(int, input().split()))

m = int(input())
for i in range(m):

    x, y = map(int,input().split())
    #print(x, y)
    if x == 1:

        while True:
            #print("dsa")
            if y > len(switch):
                #print("break")
                break
            #print('y',y)
            change(y)
            y *= 2
    elif x == 2:
        i=1
        change(y)

        while True:
            if y  - i >= 1 and y + i <= len(switch):
                if switch[y - i] == switch[y  + i]:
                    change(y-i)
                    change(y+i)


                else:
                    break
                i += 1
            else:
                break
    else:
        break



for i in range(1,len(switch)):

    if (i)%20==0:
        print()
    print(switch[i], end=" ")
#