import itertools
from itertools import permutations

n=int(input())
num=[1,2,3,4,5,6,7,8,9]
nums=list(itertools.permutations(num,3));

for i in range(n):
    q,strike,ball=map(int,input().split())
    q=list(str(q))
    remove_count=0
    for j in range(len(nums)):
        s=0
        b=0
        j -= remove_count
        for x in range(3):
            if q[x] == str(nums[j][x]):
                s+=1
            elif q[x] in str(nums[j]):
                b+=1
        if (strike != s) or (ball != b):  # 입력받은 s,b와 다르면 num에서 삭제
            nums.remove(nums[j])
            remove_count += 1
print(len(nums))

