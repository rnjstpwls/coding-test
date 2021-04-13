import sys
from collections import deque


def make_wall(idx, cnt):
    if cnt == 3:
        global result
        result = max(search(), result)
        return
    if idx == N * M:
        return

    row, col = idx // M, idx % M

    if arr[row][col] == 0:
        arr[row][col] = 1
        make_wall(idx + 1, cnt + 1)
        arr[row][col] = 0
    make_wall(idx + 1, cnt)


def search():
    visited = [[False] * M for _ in range(N)]
    visit = 0
    q = deque()
    for r, c in virus:
        visited[r][c] = True
        visit += 1
        q.append((r, c))
    while q:
        cr, cc = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if (0 <= nr < N) and (0 <= nc < M) and not arr[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                visit += 1
                q.append((nr, nc))
    return N * M - visit - cnt


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))
virus = []
cnt = 3
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            virus.append((r, c))
        elif arr[r][c] == 1:
            cnt += 1

result = 0

make_wall(0, 0)
print(result)
