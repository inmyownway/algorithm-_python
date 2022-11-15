from collections import deque

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # pw =      2 3 8 0 9 9 0 8 4
    # new_list =1
    new_list =[]
    n,p=input().split()

    n=int(n)
    pw = deque(p)

    new_list.append(pw.popleft())
    for i in range(1,n):
        if len(new_list)==0:
            new_list.append(pw.popleft())
            continue
        temp = pw.popleft()
        #rint("temp: ",temp)

        if new_list[-1] == temp:
            new_list.pop()
        else:
            new_list.append(temp)
    #print(new_list)





    print("#%d %s"%(test_case,''.join(new_list)))