def rotate(r):
    n=len(r)
    m=len(r[0])
    result=[[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(m):
            result[b][n - 1 - a] = r[a][b]

    return result

def check(new_lock):
    l = len(new_lock)//3
    for i in range(l,l*2):
        for j in range(l,l*2):
            if new_lock[l][j]!=1:
                return False
    return True

def solution(key, lock):
    n= len(lock)
    m= len(key)

    new_lock = [[0]* (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    for i in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False











key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))