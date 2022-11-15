from collections import deque
n=int(input())
for i in range(1,n+1):
    n=int(input())

    words = list((input().split()))
    # 1 2 3 4 5 6
    if len(words)%2==0:
        front= words[0:(len(words)//2)]
        back = words[(len(words)//2):]
    else:
        front= words[0:(len(words)//2)+1]
        back = words[(len(words) // 2)+1:]
    #print(front,back)
    new=[]
    front= deque(front)
    back = deque(back)
    while True:
        if len(front)==0 and len(back )==0:
            print("#%d %s"%(i,' '.join(new)))
            break
        if front:
            new.append(front.popleft())
        if back:
            new.append(back.popleft())


