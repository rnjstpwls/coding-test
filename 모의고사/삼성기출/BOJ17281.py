import sys
from itertools import permutations

def search(order):

    current = 0
    round = 0

    score = 0
    while round < N:
        b1, b2, b3 = 0, 0, 0
        out_cnt = 0
        while out_cnt < 3:
            tmp = arr[round][order[current]]
            if tmp == 0:
                out_cnt += 1
            elif tmp == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif tmp == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif tmp == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            current = (current + 1) % 9
        round += 1

    return score

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

case = list(permutations(range(1, 9), 8))
result = 0
for c in case:
    c = list(c)
    result = max(search(c[0:3] + [0] + c[3:8]), result)
print(result)