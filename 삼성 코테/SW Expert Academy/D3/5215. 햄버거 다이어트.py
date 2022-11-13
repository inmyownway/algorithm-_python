from itertools import combinations
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,l=map(int,input().split())
    data =[list(map(int,input().split())) for _ in range(n)]

    max = 0

    for i in range(1,n+1):
        for value in combinations(data,i):
          kcal =0
          score =0
          for v in range(len(value)):
              kcal += value[v][1]
              score +=value[v][0]
          if kcal > l:
              continue
          if max < score:
              max = score
    print("#%d %d" %(test_case,max))


