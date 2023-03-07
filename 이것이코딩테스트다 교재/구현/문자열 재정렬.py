n=list(input())

n.sort()

sum=0
str1=""

for i in n:
    if i.isalpha():
        str1+=i
    else:
        sum+=int(i)

print(str1+str(sum))
