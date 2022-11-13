

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    l=int(input())
    m=[]
    count=0
    for i in range(8):
        m.append(list((input())))
    #print(m)
    for i in range(8):
        for j in range(0,8-l+1):
            temp = m[i][j:j+l]
            if temp == temp[::-1]:
                #print(temp)
                count+=1
        temp =""
        for j in range(0,8-l+1):
            for x in range(l):
                temp += str(m[x+j][i])
                #
            if temp == temp[::-1]:
                count+=1
                #print("sero ",temp)
            temp=""
    print("#%d %d"%(test_case,count))