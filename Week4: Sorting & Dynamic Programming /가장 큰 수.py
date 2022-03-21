from itertools import permutations
def solution(numbers):
    sum = ''
    max = 0
    for i in permutations(numbers,len(numbers)):
        for j in i:
            sum += str(j)
        if int(sum) > max:
            max = int(sum)
        sum = ''
    return str(max)
