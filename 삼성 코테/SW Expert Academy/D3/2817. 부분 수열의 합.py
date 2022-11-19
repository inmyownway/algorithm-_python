T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,k=map(int,input().split())
    seq=list(map(int,input().split()))

    count=0
    for i in range(n):
        for j in range(i+1,n):
            if seq[i]+seq[j]==k:
                count+=1
    print("#%d %d"%(test_case,count))
