from itertools import permutations
n=int(input())
l=[]
for i in range(n):
    temp=list(input().split())
    l.append(temp)
nums=['1','2','3','4','5','6','7','8','9']
number=list(permutations(nums,3))

cnt =0
#print(l)
for num in number:

    flag=0
    for i in range(n):
        s,b=0,0


        guess=l[i][0]
        #print(guess,num)
        for j in range(3):
            #print((guess[1]))
            if guess[j]==num[j]:
                s+=1
            else:
                if num[j] in guess:
                    b+=1
        if str(s)!= l[i][1] or str(b)!=l[i][2]:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        cnt+=1
print(cnt)
