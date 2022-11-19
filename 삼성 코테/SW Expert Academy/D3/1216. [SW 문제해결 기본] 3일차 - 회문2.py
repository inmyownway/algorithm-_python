
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10+ 1):
    n=int(input())
    pw=list(input().split())
    order=list(input().split())
    orders=list((input().split()))
    print(pw)
    for i in range (len(orders)):
        if order[i]=='I':
            ind=orders[i+1]
            o = orders[i+2:orders[i+2]+1]
            i+=7
            temp1 =pw[:ind]
            temp2=pw[ind:]
            print(temp1)
            print(temp2)
            for j in o:
                temp1.append(j)
            temp1.append(temp2)
    print(temp1)


    print(orders)
