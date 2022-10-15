
n = int(input())

l=[]
for i in range (n):

    l.append( int(input()))

d = [0]*n

# 1 6 8 9 10 13

if len(l)== 1:
    print(l[0])
elif len(l)==2:
    print(l[0]+l[1])
else:
    d[0]=l[0] # d[0]=1
    d[1]=l[0]+l[1] # d[1] =7
    d[2]=max(l[0],l[1])+l[2] # d[2]= 14
    # l= [1,6,8,9,10,13]
    # d= [1,7,14,18]
    #
    # i-2 번까지 최대로 마시고 현재잔 i 마시기
    # i-3 번까지 최대로 마시고 + i-1 과 현재잔 i 마시기
    # i-4 번까지 최대로 마시고 + i-1 과 현재잔 i 마시기
    for i in range(3,n):
        d[i]= max(d[i-2]+l[i] , d[i-3]+l[i-1]+l[i] , d[i-4]+l[i-1]+l[i])
    print(max(d))
