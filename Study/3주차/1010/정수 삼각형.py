from collections import deque
triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

# 7
# 10 15
# 18 11 16 15
# 20 25 18 15 23 20  19 19
# 24 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14

result_list = [[] for i in range (len(triangle))]


result_list[0].append(triangle[0][0])
for i in range (1,len(triangle)):
    temp = 0
    l =deque()
    ab = 0
    for x in range (len(result_list[i-1])):
        l.append(result_list[i-1][x])
    print(l)

    ab = 0
    while True:
        if(len(l)==0):
            break
        t = l.popleft()
        print(t)


        print(t,"+",triangle[i][ab])
        print(t,"+",triangle[i][ab+1])
        temp1 = t + triangle[i][ab]
        temp2 = t + triangle[i][ab+1]
        ab += 1

        print(temp1," ",temp2)
        result_list[i].append(temp1)
        result_list[i].append(temp2)

        temp1=0
        temp2=0
        print(result_list)


print(result_list)
