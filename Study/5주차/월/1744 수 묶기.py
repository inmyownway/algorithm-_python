n= int(input())

pos=[]
neg=[]
# sum = 1
# 4 3 2
# -1
sum=0
# 4 3 2 1 -1
for i in range((n)):
    num=int(input())
    if num > 1:
        pos.append(num)
    elif num ==1:
        sum+=1
    else:
        neg.append(num)

pos.sort(reverse=True)
neg.sort()

if len(pos)%2 == 0: # 길이 짝수
    for i in range(0,len(pos),2):
        sum+=pos[i]*pos[i+1]
else:
    for i in range(0,len(pos)-1,2):
        sum += pos[i] * pos[i + 1]
    sum+=pos[len(pos)-1]


if len(neg)%2 == 0: # 길이 짝수
    for i in range(0,len(neg),2):
        sum+=neg[i]*neg[i+1]
else:
    for i in range(0,len(neg)-1,2):
        sum += neg[i] * neg[i + 1]
    sum+=neg[len(neg)-1]

print(sum)