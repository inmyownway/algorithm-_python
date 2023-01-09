
n,m,k = map(int,input().split())
nums= list(map(int,input().split()))


nums.sort(reverse=True)
sum=0
# 내 풀이
# for i in range(1,m+1):
#     if i//k !=0:
#         sum+=nums[0]
#     elif i//k==0:
#         sum+=nums[1]
# print(sum)

# 교재 코드1
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         sum+=nums[0]
#         m-=1
#     if m==0:
#         break
#     sum+=nums[1]
#     m-=1

print(sum)