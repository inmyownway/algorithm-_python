# h,w=map(int,input().split())
# n=list(map(int,input().split()))
# # n = [3,0,1,4]
# world=[[0]*w for _ in range(h)]
# for i in range(len(n)):
#     for j in range(n[i]): # j = 0,1,2
#         world[h-1-j][i]=1
#
# #print(world)

# sum=0
# for i in range(h):
#     wall=0
#     rain=0
#     for j in range(w):
#
#         if world[i][j]==1:
#             wall+=1
#         if wall == 2:
#             sum += rain
#             rain = 0
#             wall = 1
#             continue
#
#         elif wall==1 and world[i][j]==0:
#             rain+=1
#     #print(rain)
#
# print(sum)
#
# 4 4
# 3 0 1 4
#
# #       1
# # 1     1
# # 1     1
# # 1 _ 1 1
h,w=map(int,input().split())
block=list(map(int,input().split()))
answer= 0

for i in range(1,w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    print(left,right)

    c=min(left,right)
    if block[i]<c:
        answer+=c-block[i]
print(answer)