

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def result(n,m):
    if m==0:
        return 1

    else:
        return n*result(n,m-1)
for test_case in range(1, 11):
    a=int(input())
    n,m= map(int,input().split())
    print("#%d %d"%(test_case,result(n,m)))
