

def bs(array,target,start,end):

    while start<=end:

        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            end=mid-1
        elif array[mid]>target:
            start=mid+1
    return None

n=int(input())
array=list(map(int,input().split()))
array.sort()
k=int(input())

targets=list(map(int,input().split()))
for target in targets:
    result= bs(array,target,0,n-1)
    if result!=None:
        print('yes',end='')
    else:
        print('no',end='')


