from itertools import combinations
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

stats = list(list(map(int, input().split())) for _ in range(N))

com = list(combinations(range(N), N//2))
length = len(com)
result = [0] * length
answer = [0] * (length // 2)
for i in range(length):
    tmp = 0
    for a, b in combinations(com[i], 2):
        tmp += stats[a][b]
        tmp += stats[b][a]
    result[i] = tmp

for i in range(length//2):
    answer[i] = abs(result[i] - result[-1-i])
print(min(answer))