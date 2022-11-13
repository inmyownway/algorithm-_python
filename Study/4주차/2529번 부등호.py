import itertools
n=int(input())
b = list((input().split()))
numbers =[0,1,2,3,4,5,6,7,8,9]

select_nums=list(itertools.permutations(numbers, n+1))
#  < >
# 1 3 5
result=[]
for nums in select_nums:
    count = 0
    for j in range(n):
        if b[j]== '>':
            if nums[j]>nums[j+1]:
                count+=1
            else:
                break
        elif b[j] == '<':
            if nums[j]<nums[j+1]:
                count+=1
            else:
                break
        if count==n:
            result.append(nums)



print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))
# for i in result:
#     s=""
#     for j in range(n+1):
#         s+=str(i[j])
#     r.append(s)
# max=result[-1]
# min=result[0]
# s=""
# c=""
# for i in max:
#     s+=str(max[i])
# for j in min:
#     c+=str(min[j])
#
# print(s)
# print(c)
#
#
