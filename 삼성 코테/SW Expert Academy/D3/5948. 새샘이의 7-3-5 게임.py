from itertools import combinations
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l=list(map(int,input().split()))
    #print(l)
    p=list(combinations(l,3))
    #print(p)
    ind=[]

    for i in p:
        ind.append(sum(i))
    ind.sort(reverse=True)
    new_list=[]
    for i in ind:
        if i not in new_list:
            new_list.append(i)
    #print(new_list)
    print("#%d %d"%(test_case,new_list[4]))