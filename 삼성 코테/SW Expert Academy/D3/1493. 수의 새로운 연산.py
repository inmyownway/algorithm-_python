
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())

    x=1
    y=1
    yy=2
    for i in range(1,10000):
        x+=i
        y+=yy
        yy+=1
        if 



