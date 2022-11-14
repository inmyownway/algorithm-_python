
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    case = list(map(int,input().split()))
    last=case[-1]
    sum=0
    # 3 5 9
    # 3 10 9
    for i in range(n-2,-1,-1):
        if last > case[i]:
            sum+= last - case[i]
        else:
            last=case[i]


    print('#{} {}'.format(test_case, sum))
