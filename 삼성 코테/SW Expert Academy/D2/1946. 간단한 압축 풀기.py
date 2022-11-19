T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    l=[]

    for i in range(n):
        str = ""
        a,b=input().split()
        for i in range(int(b)):
            str+=a
        l.append(str)
    #print("#%d"%(test_case))
    s=0
    ind=10
    #print(l)
    temp =''.join(l)
    #print(temp)

    a=0
    b=10
    print("#%d"%(test_case))
    for i in range((len(temp)//10)+1):
        print(temp[a:b])
        a+=10
        b+=10
