n,m=map(int,input().split())
result = 0
# 내 코드
# group=[]
# for i in range(n):
#     temp=list(map(int,input().split()))
#     temp.sort()
#     group.append(temp)
#
# for i in range(n):
#     if max < group[i][0]:
#         max = group[i][0]


# 교재 코드 1
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)
print(result)