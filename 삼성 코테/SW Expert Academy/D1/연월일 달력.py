
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cal = input()

    y = cal[0:4]
    d_m=cal[4:6]
    d_d=cal[6:]
    m=int(cal[4:6])
    d=int(cal[6:])


    if m < 1 or m >12:
        print("#%d -1"%test_case)
        continue

    if m == 1 or m == 5 or m==3 or  m==7 or m==8 or m==10 or m ==12:
        if d < 0 or d > 31:
            print("#%d -1" % test_case)
            continue
    if m==2:
        if d < 0 or d > 28:
            print("#%d -1" % test_case)
            continue
    if m == 4 or m == 6 or m==9 or  m==11:
        if d < 0 or d > 30:
            print("#%d -1" % test_case)
            continue

    print("#%d"%(test_case),y+"/"+d_m+"/"+d_d)





