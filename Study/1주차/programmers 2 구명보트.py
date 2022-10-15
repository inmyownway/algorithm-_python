def solution(people, limit):
    count = 0
    people.sort(reverse=True)
    start=0
    end=len(people)-1

    while True:
        temp = people[start]+people[end]
        if(start>=end):
            break
        if(temp > limit):
            count+=1
            start+=1
        else:
            count+=1
            start+=1
            end-=1

    if(start==end):
        count+=1
    return count