T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l,u,x=map(int,input().split())

    if l > x:
        answer = l-x
    elif x > u:
        answer =-1
    elif x >=l:
        answer = 0

    print("#%d %d"%(test_case,answer))
