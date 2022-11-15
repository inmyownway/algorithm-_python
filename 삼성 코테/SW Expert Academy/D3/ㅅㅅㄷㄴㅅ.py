from collections import deque

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # 1 2 3 8 0 9 9 0 8 4
    # 1 2 3 8 0
    new_list = []
    n, p = input().split()

    print(n)
    # print("#%d %d",(test_case,))