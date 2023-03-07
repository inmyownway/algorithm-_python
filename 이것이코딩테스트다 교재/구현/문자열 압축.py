def solution(s):
    answer =len(s)

    for step in range(1,len(s)//2+1):

        sen=""
        prev = s[0:step]
        count = 1
        for j in range(step,len(s),step):
            if prev==s[j:j+step]:
                count+=1
            else:
                sen+=str(count)+prev if count >=2 else prev
                prev=s[j:j+step]
                count=1
        if count >=2:
            sen+=str(count)+prev
        else:
            sen+=prev
        answer= min(answer,len(sen))
    return answer


solution("aaaabbabbabb")

