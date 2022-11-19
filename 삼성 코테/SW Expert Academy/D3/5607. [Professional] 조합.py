from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word_list=[]

    for a in range(5):
        word_list.append(list(input()))
    max_len=0

    for i in word_list:
        if max_len <len(i):
            max_len=len(i)

    result=[[] for _ in range(max_len)]

    # A A A A A  i = 0~4
    # B B B     len =4
    # C C C C C
    # D D D D D
    # E E E E
    for i in range (max_len):
        for j in range (5):
            if i < len(word_list[j]):
                result[i].append(word_list[j][i])

        #print(result)

    str=""
    for i in result:
        for j in i:
            str+=''.join(j)
    print("#%d %s"%(test_case,str))
