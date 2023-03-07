from itertools import permutations
n=int(input())
nums=['0','1','2','3','4','5','6','7','8','9']
l=list(input().split())
numbers=permutations(nums,n+1)
result=[]
for num in numbers:
    #print(num)
    str=""
    flag=True
    for i in range(len(num)-1): # 0 1
        if l[i]=='>':
            if int(num[i])>int(num[i+1]):
                str+=num[i]
            else:
                i=len(num)
                flag=False
        elif l[i]=='<':
            if int(num[i]) < int(num[i + 1]):
                str += num[i]
            else:
                i=len(num)
                flag=False
    if flag:
        str+=num[-1]
        result.append(str)
print(result[-1])
print(result[0])
