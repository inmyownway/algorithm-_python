n=input()


x1=[1,-1,1,-1]
y1=[2,2,-2,-2]

y2=[1,-1,1,-1]
x2=[2,2,-2,-2]

count=0
al= ['no','a','b','c','d','e','f','g','h']

cx=0
cy=0
for i in range(len(al)):
    if al[i]==n[0]:
        cy=i
cx=int(n[1])
tx=0
ty=0
print("  asdas",cx,cy)
for i in range(0,4):
    tx = cx+x1[i]
    ty = cy+y1[i]
    if 1<= tx <= 8 and 1<= ty <= 8:
        print(tx,ty)
        count+=1
for i in range(4):
    tx = cx+x2[i]
    ty = cy+y2[i]
    if 1 <= tx <= 8 and 1 <= ty <= 8:
        print(tx, ty)
        count += 1
print(count)
