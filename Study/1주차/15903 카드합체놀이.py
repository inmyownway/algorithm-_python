
n,m=map(int,input().split())
card= list(map(int,input().split()))


for i in range(0,m):
    card.sort(reverse=True)
    min1= card.pop()
    min2=card.pop()
    temp = min1+min2
    card.append(temp)
    card.append(temp)

print(sum(card))


