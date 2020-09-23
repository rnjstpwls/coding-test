import sys
sys.stdin = open('input.txt')

C, R = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
if K > C*R:
    print(0)
    exit()
if K == 1:
    print(1, 1)
    exit()
arr = [[0]*C for _ in range(R)]

r, c = R-1, 0
value = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
dir = 0

arr[r][c] = value
value += 1
while True:
    r, c = r+dr[dir], c+dc[dir]
    if not(0 <= r <= R-1) or not(0 <= c <= C-1) or arr[r][c]:
        r, c = r-dr[dir], c-dc[dir]
        dir = (dir+1) % 4
        continue
    arr[r][c] = value
    if value == K:
        result = (c+1, R-r)
        break
    value += 1

print(*result)