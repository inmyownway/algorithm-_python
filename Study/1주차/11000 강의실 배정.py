import sys
import heapq

n= int(input())
l=[]
for i in range(0,n):
    s,t = map(int,input().split())
    l.append([s,t])
l.sort()


new_list =[]
heapq.heappush(new_list,l[0][1])

for i in range(1,n):

    if l[i][0] < new_list[0]: # 끝나는시간보다 시작시간이 일찍임
        heapq.heappush(new_list,l[i][1])
    else:
        heapq.heappop(new_list)
        heapq.heappush(new_list,l[i][1])


ㅈ
print(len(new_list))
