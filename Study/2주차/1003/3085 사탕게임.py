
n= int(input())
b = [list(input()) for _ in range(n)]
maxCount=0

def check():
    global maxCount
    for i in range(n):
        count = 1
        for j in range(1,n):
            if b[i][j] == b[i][j-1]:
                count+=1
                maxCount = max(count,maxCount)
            else:
                count = 1
        count = 1
        for j in range(1,n):
            if b[j][i] == b[j-1][i]:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 1

for i in range (n):
    for j in range(n-1):
        if j+1 <n: # 행
            b[i][j],b[i][j+1] = b[i][j+1],b[i][j]
            check()
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        if i+1 <n: # 열
            b[i][j],b[i+1][j]= b[i+1][j],b[i][j]
            check()
            b[i][j], b[i + 1][j] = b[i + 1][j], b[i][j]

print(maxCount)