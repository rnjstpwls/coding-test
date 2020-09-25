import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

idx = []
height = []

for _ in range(N):
    i, h = map(int, sys.stdin.readline().split())
    idx.append(i)
    height.append(h)

start, last = min(idx), max(idx)

max_height = max(height)
max_idx = idx[height.index(max_height)]

result = 0
value = height[idx.index(start)]
for i in range(start, max_idx):
    if i in idx:
        if height[idx.index(i)] > value:
            value = height[idx.index(i)]
    result += value

value = height[idx.index(last)]
for i in range(last, max_idx, -1):
    if i in idx:
        if height[idx.index(i)] > value:
            value = height[idx.index(i)]
    result += value

print(result+max_height)