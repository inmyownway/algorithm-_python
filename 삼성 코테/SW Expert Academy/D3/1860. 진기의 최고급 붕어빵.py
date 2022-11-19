T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m,k=map(int,input().split())
    # m초동안 k개 만듬
    fish=0
    client=list(map(int,input().split()))
    client.sort()

    check = "Possible"
    for i in range(n):
        fish = (client[i]//m)*k -(i+1)
        if fish <0:
            check="Impossible"

    print("#%d %s"%(test_case,check))


