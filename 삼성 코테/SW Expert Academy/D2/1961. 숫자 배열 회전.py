T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    nums=[]
    for i in range(n):
        nums.append(list(map(int,input().split())))

    list90=[[0]*n for _ in range(n)]
    list180 = [[0] * n for _ in range(n)]
    list270=[[0]*n for _ in range(n)]
    # 90 도
    for i in range(n):
        for j in range(n):
            list90[i][j]=nums[n-1-j][i]
        # 90 도
    for i in range(n):
        for j in range(n):
            list180[i][j] = list90[n - 1 - j][i]
        # 90 도
    for i in range(n):
        for j in range(n):
            list270[i][j] = list180[n - 1 - j][i]

    print("#%d"%(test_case))
    for i in range(n):
        for j in range(n):
            print(list90[i][j],end="")
        print(end=" ")
        for j in range(n):
            print(list180[i][j],end="")
        print(end=" ")
        for j in range(n):
            print(list270[i][j], end="")
        print()

            # print(list180[i][j], end="")
            # print(list270[i][j], end=" ")


