import itertools
from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num,c=input().split()
    ca=num
    num=list(num)
    c=int(c)
    #print(num)
    l=list(itertools.permutations(num,len(num)))
    #print(l)
    check =[]

    for a in l:
        temp = ""
        # print("a:",a)
        for b in range(len(a)):
            temp += a[b]
        # print("temp: ",temp)
        check.append(int(temp))
    #print(max(check),ca)
    if int(max(check)) == int(ca) or len(num)<=int(c):
        print("#%d %d"%(test_case,max(check)))
        continue


    result=[]
    # 32888
    # 88832
    # c=2
    for i in l:
        count=0
        for j in range(len(i)):
            if num[j]!=i[j]:
                count+=1
        if count==c*2:
            result.append(i)

    last=[]
    for a in result:
        temp=""
        #print("a:",a)
        for b in range (len(a)):
            temp +=a[b]
        #print("temp: ",temp)
        last.append(int(temp))
    print("#%d %d"%(test_case,max(last)))



