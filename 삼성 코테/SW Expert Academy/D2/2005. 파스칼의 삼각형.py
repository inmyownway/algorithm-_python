t=int(input())
for test_case in range(1,t+1):
    n=int(input())
    matrix =[[0]*n for _ in range(n)]

    # 1 0 0 0
    # 1 1 0 0
    # 1 0 0 0
    # 0 0 0 0
    for i in range (n):
        for j in range(i+1):
            if j==0 or j==i:
                matrix[i][j]=1
            else:
                matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]

    print("#%d"%(test_case))
    #print(matrix)
    for i in matrix:
        for j in i:
            if j!=0:
                print(j,end=" ")
        print()


