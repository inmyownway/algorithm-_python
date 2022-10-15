import itertools
L,C=map(int,input().split())


group=list(map(str,input().split()))
group.sort()
new_group = itertools.combinations(group,L)
password=[]
result=[]

for temp in list(new_group):
    str=""
    for j in range(L):
        str+=temp[j]
    password.append(str)




for i in password:

    count1 = 0
    count2 = 0
    # 오름 차순 확인
    for j in range(0,L-1):
        if ord(i[j])> ord(i[j+1]):
            count1+=1
    # 모음 개수 확인
    for x in range(L):
        if i[x]=='a' or i[x]=='e' or i[x]=='o' or i[x]=='u'or i[x]=="i":
            count2+=1
    # 자음 개수 확인
    l = len(i)-count2
    if count1==0 and count2 >=1 and l>=2:
        result.append(i)



result.sort()
for i in result:
    print(i)



