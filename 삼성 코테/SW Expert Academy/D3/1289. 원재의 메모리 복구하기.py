T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    first = input()
    zero=[]
    count = 0

    for i in range(len(first)):
        zero.append('0')

    # 0011
    # 0000
    for i in range(len(first)):
        if zero[i]==first[i]:
            continue
        else:
            count+=1
            for j in range(i,len(first)):
                zero[j]=first[i]
    print("#%d %d"%(test_case, count))

