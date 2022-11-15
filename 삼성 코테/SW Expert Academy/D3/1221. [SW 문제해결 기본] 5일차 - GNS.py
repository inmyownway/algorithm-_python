
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
l = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(1, T + 1):
    result=[]
    new=[]
    n,m=input().split()

    nums = list(input().split())
    for i in nums:
        if i in l:
            temp =l.index(i)
            result.append(temp)
    result.sort()
    for j in result:
        new.append(l[j])
    print(n)
    print(' '.join(new))

