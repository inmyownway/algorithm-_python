
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,11):
    matrix=[]
    T = int(input())
    for i in range(0,100):
        matrix.append(list(map(int,input().split())))


    max=-1

    # 가로
    for i in range(0,100):
        sum = 0
        for j in matrix[i]:
            sum+=j
        if max < sum:
            max= sum

    # 세로
    for a in range(0,100):
        # 각 열의 합을 구하는 c_total 변수 초기화
        sum = 0
        # 각 열의 합을 구하고, 그 값을 col_total_list 에 추가
        for b in range(0,100):
            sum += matrix[b][a]
        if max < sum:
            max = sum
    # 왼쪽 대각
    sum=0
    for i in range(0,100):

        sum += matrix[i][i]
    if max < sum:
        max = sum
    # 오른쪽 대간
    j=99
    sum=0
    for i in range(0,100):
       sum+=matrix[i][j]
       j-=1
    if max < sum:
        max = sum
    print("#%d %d" %(test_case,max))








