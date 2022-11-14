
n =int(input())
arr=[]
for i in range(1,n+1):
    clap=""
    temp=[]
    j=str(i)
    for x in range(len(j)):
        if j[x]=="3":
            clap+="-"
        if j[x] == "6":
            clap += "-"
        if j[x] == "9":
            clap += "-"
    if len(clap) >=1:
        arr.append(clap)
    else:
        arr.append(i)

for i in arr:
    print(i,end=" ")

