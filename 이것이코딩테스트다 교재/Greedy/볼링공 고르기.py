#from itertools import combinations
n,m=map(int,input().split())

w=list(map(int,input().split()))
l=[]
# for i in range (len(w)-1):
#     for j in range (i+1,len(w)):
#         if w[i]!=w[j]:
#             l.append([w[i],w[j]])
# print(len(l))

array=[0]* 11
for i in range(len(w)):
    array[w[i]]+=1
print(array)
# 1 2 2 3 3
result= 0
for i in range(1,m+1):
    n-=array[i]
    print(array[i]*n)
    result+= array[i]*n
# -1 + 5 , -2 + 10 , -2
print(result)
