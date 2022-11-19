
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())

    matrix=[]

    for i in range(n):
        matrix.append(list(map(int,input().split())))
    #print(matrix)
    max = -1
    for i in range (n-m+1):

        sum=0
        for j in range(n-m+1):
            sum=0
            #print("i,j:",i,j)
            for a in range(m):
                for b in range(m):
                    #print(i+a,j+b)
                    sum+=matrix[i+a][j+b]
            if max <sum:
                max=sum
    print("#%d %d"%(test_case,max))

