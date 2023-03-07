from itertools import permutations
n=int(input())
nums=list(map(int,input().split()))

y=[]
p= list(map(int,input().split()))
for i in range(p[0]):
    y.append('+')
for i in range(p[1]):
    y.append('-')
for i in range(p[2]):
    y.append('*')
for i in range(p[3]):
    y.append('/')

yy =set(permutations(y,len(y)))
#print(yy)
sum=0
min=1e9
max=-1e9

temp= []
for ys in (yy):
    #print(" ",ys)
    sum = nums[0]

    for i in range(len(ys)):
        #print(ys[i])
        if ys[i]=='+':
            sum+=nums[i+1]
        elif ys[i]=='-':
            sum-=nums[i+1]
        elif ys[i]=='*':
            sum *= nums[i+1]
        elif ys[i]=='/':
            if sum <0:
                sum=sum*-1
                sum=sum//nums[i+1]
                sum=sum*-1
            else:
                sum=sum//nums[i+1]
        #print(sum)

    if sum>max:
        max = sum
    if sum < min:
        min=sum

print(max)
print(min)