from sys import stdin
n = int(input())
for z in range(0,n):

    day = int(stdin.readline())
    m =  list(map(int, stdin.readline().split()))

    sum = 0
    my=[]

    for i in range(0,day):
        count=0
        for j in range(i+1,day):
            if(m[i]<m[j]):
                count+=1
        if count >= 1:
            my.append(m[i])  # 오늘 주식이 나머지 날 주식보다 작으면 구매
        if len(my)>=1:
            if my[-1] < m[i]:
                while my:
                    sum+=m[i]-my.pop() # 가지고있는 주식중에 가장 큰게 그날의 주식보다 작으면
                                       # 가지고 있는거 그날 다 판매
    print(sum)