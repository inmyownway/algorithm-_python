# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n=int(input())
    l=list(map(int,input().split()))
    count =0
    for i in range(2,len(l)-2):
        temp = l[i]-max(l[i-1],l[i-2],l[i+1],l[i+2])
        if temp >0:
            count+=temp

    print("#%d %d"%(test_case,count))