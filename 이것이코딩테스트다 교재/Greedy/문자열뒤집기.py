data=input()
one=0
zero=0


if data[0]==1:
    zero+=1
else:
    one+=1

# 0 0 0 1 1 0 0

# zero = 1
#
for i in range(len(data)-1):
    if data[i] !=data[i+1]:
#    다음수에서 1로 바뀌는경우
        if data[i+1]=='1':
            zero+=1
        else:
            one+=1


