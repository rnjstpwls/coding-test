import sys


def search(r, c, length, chance):
    global result
    result = max(result, length)
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if (0 <= nr < N) and (0 <= nc < N) and not visited[nr][nc]:
            if arr[nr][nc] < arr[r][c]:
                visited[nr][nc] = True
                search(nr, nc, length + 1, chance)
                visited[nr][nc] = False
            elif chance and arr[nr][nc] - K < arr[r][c]:
                visited[nr][nc] = True
                storage = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                search(nr, nc, length + 1, False)
                visited[nr][nc] = False
                arr[nr][nc] = storage


sys.stdin = open('input.txt')

T = int(input())

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_height = 0
    for r in range(N):
        max_height = max(max_height, max(arr[r]))

    visited = [[False] * N for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_height:
                visited[r][c] = True
                search(r, c, 1, True)
                visited[r][c] = False

    print('#{} {}' .format(tc, result))