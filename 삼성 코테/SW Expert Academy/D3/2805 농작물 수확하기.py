

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    map = []
    for i in range(n):
        temp =list(input())

        temp2 = [int(i) for i in temp]

        map.append(temp2)
    #print(map)
    start=(n//2)
    end =start+1
    result=0
    for j in range(1,n+1):
        t=map[j-1][start:end]
        #print(sum(t))
        result+=sum(t)
        if j<= (n//2):
            start-=1
            end+=1
        elif j > (n//2):
            start+=1
            end-=1
    print("#%d %d"%(test_case,result))