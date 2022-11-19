T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    submit=list(map(int,input().split()))
    #print("submit: ",submit)
    all=[]
    for i in range(1,n+1):
        if i not in submit:
            all.append(i)
    toStr= list(map(str,all))
    print("#%d %s"%(test_case,' '.join(toStr)))
