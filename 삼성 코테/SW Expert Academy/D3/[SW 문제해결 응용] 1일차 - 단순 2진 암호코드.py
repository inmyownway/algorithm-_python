
T = int(input())
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    for i in range (n):
        temp = list((input()))
        temp = ''.join(reversed(temp))
        for t in range(len(temp)):
            if temp[t] == '1':
                #print(t)

                result = temp[t:t+56]

                result = ''.join(reversed(result))
                break

    str = ''.join(result)
    #print(str,len(str))
    l=[]
    a=0
    for i in range (0,8):

        l.append(str[a:a+7])
        a+=7
    #print(l)
    new_l=[]
    flag=0
    for j in l:
        #print(j)
        if j == '0001101':
           new_l.append(0)
        elif j == '0011001':
            new_l.append(1)
        elif j == '0010011':
            new_l.append(2)
        elif j == '0111101':
            new_l.append(3)
        elif j == '0100011':
            new_l.append(4)
        elif j == '0110001':
            new_l.append(5)
        elif j == '0101111':
            new_l.append(6)
        elif j == '0111011':
            new_l.append(7)
        elif j == '0110111':
            new_l.append(8)
        elif j == '0001011':
            new_l.append(9)
        else:
            flag=1
# 0100110/1000110/1100010/0011010/1000110/1000110/0011010/001011
# 00100110100011011000100011010100011010001100011010001011
    #print(new_l)
    if flag == 1:
        print("#%d 0" % (test_case))
    elif ((new_l[0]+new_l[2]+new_l[4]+new_l[6])*3 + (new_l[1]+new_l[3]+new_l[5]+new_l[7])) % 10 == 0:
        print("#%d %d" %(test_case,sum(new_l)))
    else:
        print("#%d 0" %(test_case))

