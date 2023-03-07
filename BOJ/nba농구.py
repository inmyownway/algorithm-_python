from collections import deque()
n=int(input())
record=[]
for i in range(n):
    x,y=input().split()
    record.append((x,y))

print(record)

record=deque(record)
first_score,first_time=record.popleft()

time_1=0
time_2=0


score_1=0
score_2=0
def change(m):
    return int(m[:2])+int(m[:3])

if first_score==1:
    score_1+=1
else:
    score_2+=1
time_1=

while record:
    time,