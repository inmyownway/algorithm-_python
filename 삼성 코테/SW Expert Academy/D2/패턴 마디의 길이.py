
test=int(input())

for test_case in range(1,test+1):
    str=input()
    check=0
    for i in range(1,10):
     # KoreaKorea


        temp = str[0:i]
        if temp == str[i:i+i]:
           print("#%d %d"%(test_case,i))
           check =1
           break
