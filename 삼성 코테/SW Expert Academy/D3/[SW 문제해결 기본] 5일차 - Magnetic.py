T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    graph = []
    count=0
    for i in range(n):
        graph.append(list(map(int,input().split())))

    new_graph=[[] for _ in range(n)]
    for i in range (n):
        for j in range(n):
            if graph[j][i] != 0:
                new_graph[i].append(graph[j][i])

    for i in range(n):
        str1= new_graph[i]
        for j in range(len(str1)-1):

            str1 = ''.join(map(str,str1))
            #print(str1[j:j + 2])
            if str1[j:j+2]== "12":
                count+=1
    print("#%d %d"%(test_case,count))
