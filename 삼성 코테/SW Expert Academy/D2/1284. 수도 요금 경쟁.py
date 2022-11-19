T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P,Q,R,S,W =map(int,input().split())
    # 8 300 100 10 250
    # W는 사용량
    # A사는 1리터당 P
    # B사는 기본요금 Q, R리터 이하인 경우 기본요금
    # 초과면 Q + S*W
    case1= P*W
    if W<=R:
        case2=Q
    else:
        case2=Q+(S*(W-R))

    print("#%d %d"%(test_case,min(case1,case2)))