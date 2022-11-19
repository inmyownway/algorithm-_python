T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    matrix=[]
    for i in range(9):
        matrix.append(list(map(int,input().split())))

        col=set()
        row=set()

        for i in range (9):
            for j in range(9):
                col.add(matrix[i][j])
                row.add[matrix[j][i]]
        if len(col) <=8 or len(row) <= 8:
            print("#%d 0"%(test_case))
            continue
    r=0
    c=0
    i=0
    check = 0



        for j in range(0,7,3):
            sum=0
            l=[]
            for x in range(3):
                temp=matrix[j+x][:3]
                l.append(temp)
            l=set(l)
            if len(l)<=8:
                check=1





