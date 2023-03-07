n, c = map(int, input().split())
s = list(map(int, input().split()))

dic = dict()

for i in s:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
print(dic)

dic= sorted(dic.items(), key=lambda x: x[1], reverse=True)

for a,b in dic:
    for i in range(b):
        print(a,end=" ")
    print(end="")

dic = sorted(dic.item(),key=lambda x: x[1])