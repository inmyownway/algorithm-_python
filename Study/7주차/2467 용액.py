import sys

n= int(input())
l =list(map(int,input().split()))

min = sys.maxsize
start = 0
end = n-1

while start < end:
    sum = l[start]+l[end]
    if abs(sum) < min:
        answer=[]
        answer.append(l[start])
        answer.append(l[end])
        min=abs(sum)
    if sum >0:
        end-=1
    elif sum<0:
        start+=1
    else:
        break


print(answer[0],answer[1])
#
# for i in range (len(l)-1):
#     for j in range(i+1,len(l)):
#         #print("i: j:",i,j)
#         if abs(l[i]+l[j]) <min:
#
#             min = abs(l[i]+l[j])
#             #print(min)
#             element = []
#             element.append(l[i])
#             element.append(l[j])
#             #print(element)
# print(element[0],element[1])

# -99 -98 -2 -1 4 98