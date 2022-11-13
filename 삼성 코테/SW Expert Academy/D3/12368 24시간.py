T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
     n,m=map(int,input().split())
     s = 0
     s+=n
     if s >= 24:
         s-=24

     s+=m
     if s >= 24:
         s-=24

     print(('#%d %d'%(test_case,s)))
