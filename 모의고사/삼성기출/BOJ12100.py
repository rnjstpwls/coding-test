import sys

def search(idx, arr):
    # print('****************************')
    # print(idx, arr)
    # print('****************************')
    global RESULT
    if idx == 5:
        tmp_result = 0
        for r in range(N):
            for c in range(N):
                tmp_result = max(tmp_result, arr[r][c])
        RESULT = max(tmp_result, RESULT)
        return

    search(idx+1, left_to_right(arr))
    search(idx+1, right_to_left(arr))
    search(idx+1, top_to_bottom(arr))
    search(idx+1, bottom_to_top(arr))


def right_to_left(arr):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        k, idx = 0, 0
        before = -1
        while k < N:
            if arr[i][k] == 0:
                k += 1
                continue
            if arr[i][k] == before:
                tmp[i][idx-1] = arr[i][k] * 2
                before = -1
                k += 1
            else:
                before = arr[i][k]
                tmp[i][idx] = arr[i][k]
                idx += 1
                k += 1
    return tmp


def left_to_right(arr):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        k, idx = N-1, N-1
        before = -1
        while k >= 0:
            if arr[i][k] == 0:
                k -= 1
                continue
            if arr[i][k] == before:
                tmp[i][idx+1] = arr[i][k] * 2
                before = -1
                k -= 1
            else:
                before = arr[i][k]
                tmp[i][idx] = arr[i][k]
                idx -= 1
                k -= 1
    return tmp


def bottom_to_top(arr):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        k, idx = 0, 0
        before = -1
        while k < N:
            if arr[k][i] == 0:
                k += 1
                continue
            if arr[k][i] == before:
                tmp[idx-1][i] = arr[k][i] * 2
                before = -1
                k += 1
            else:
                before = arr[k][i]
                tmp[idx][i] = arr[k][i]
                idx += 1
                k += 1
    return tmp


def top_to_bottom(arr):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        k, idx = N-1, N-1
        before = -1
        while k >= 0:
            if arr[k][i] == 0:
                k -= 1
                continue
            if arr[k][i] == before:
                tmp[idx+1][i] = arr[k][i] * 2
                before = -1
                k -= 1
            else:
                before = arr[k][i]
                tmp[idx][i] = arr[k][i]
                idx -= 1
                k -= 1
    return tmp

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
RESULT = 0
board = list(list(map(int, input().split())) for _ in range(N))

search(0, board)
print(RESULT)