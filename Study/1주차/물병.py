from collections import deque

n,k=map(int,input().split())

bottle=[]
queue=deque(bottle)
for i in range(0,n):
    queue.append(1)
print(queue)
while True:
    if(len(queue)<=2):
        break
    temp1 = queue.popleft()
    temp2= queue.popleft()
    if (temp1+temp2)%2==0:
        queue.append(temp1+temp2)
    else:
        queue.append(temp1)
        queue.append(temp2)
print(queue)
