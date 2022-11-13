

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    T = int(input())
    want=input()
    str= input()
    result =[]

    count = 0
    for i in range(len(str)):
        result.append(str[i:i+len(want)])
    for t in result:
        if t == want:
            count+=1

    # count =0
    # flag=0
    # for i in range (0,len(str)):
    #     if str[i] == want[0]:
    #         flag=0
    #         for j in range(len(want)):
    #             if i!=len(str)-1:
    #                 if str[i+j]==want[j]:
    #                     flag+=1
    #         if flag == len(want):
    #             count+=1
    print("#%d %d"%(test_case,count))
