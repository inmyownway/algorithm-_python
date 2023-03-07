
n= int(input())

l=[]
for i in range(n):
    info =list((input().split()))
    l.append(info)

l.sort(key=lambda x: (-int(x[1]), int(x[2]),-int(x[3]),x[0]))

for s in l:
    print(s[0])