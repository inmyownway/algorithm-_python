
n=int(input())

count = 0

h=0
m=0
s=0
while True:
    if h==n and m==59 and s== 59:
        print(count)
        break
    s+=1

    if '3' in str(h) or '3' in str(m) or '3' in str(s):
        count+=1

    if s==60:
        m+=1
        s=0
    if m==60:
        h+=1
        m=0
    print(h," " ,m, " ",s)
