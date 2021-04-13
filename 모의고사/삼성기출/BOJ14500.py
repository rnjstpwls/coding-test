import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))
result = 0
for r in range(N):
    for c in range(M-3):
        result = max(arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r][c+3], result)

for c in range(M):
    for r in range(N-3):
        result = max(arr[r][c]+arr[r+1][c]+arr[r+2][c]+arr[r+3][c], result)

for r in range(N-1):
    for c in range(M-1):
        result = max(arr[r][c]+arr[r][c+1]+arr[r+1][c]+arr[r+1][c+1], result)


for r in range(N-1):
    for c in range(M-2):
        result = max(arr[r][c+1]+arr[r+1][c+1] + max(arr[r][c]+arr[r+1][c+2], arr[r][c+2]+arr[r+1][c]), result)

for r in range(N-2):
    for c in range(M-1):
        result = max(arr[r+1][c]+arr[r+1][c+1] + max(arr[r][c]+arr[r+2][c+1], arr[r][c+1]+arr[r+2][c]), result)

for c in range(M-2):
    result = max(arr[0][c]+arr[0][c+1]+arr[0][c+2] + max(arr[1][c], arr[1][c+1], arr[1][c+2]), result)
    result = max(arr[N-1][c] + arr[N-1][c+1] + arr[N-1][c+2] + max(arr[N-2][c], arr[N-2][c+1], arr[N-2][c+2]), result)

for r in range(N-2):
    result = max(arr[r][0] + arr[r+1][0] + arr[r+2][0] + max(arr[r][1], arr[r+1][1], arr[r+2][1]), result)
    result = max(arr[r][M-1] + arr[r+1][M-1] + arr[r+2][M-1] + max(arr[r][M-2], arr[r+1][M-2], arr[r+2][M-2]), result)

for r in range(N-2):
    for c in range(M-2):
        result = max(arr[r+1][c]+arr[r+1][c+1]+arr[r+1][c+2] + max(arr[r][c], arr[r][c+1], arr[r][c+2], arr[r+2][c], arr[r+2][c+1], arr[r+2][c+2]), result)

for c in range(M-2):
    for r in range(N-2):
        result = max(arr[r][c+1]+arr[r+1][c+1]+arr[r+2][c+1] + max(arr[r][c], arr[r+1][c], arr[r+2][c], arr[r][c+2], arr[r+1][c+2], arr[r+2][c+2]), result)

print(result)