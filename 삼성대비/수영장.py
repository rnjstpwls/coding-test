import sys
sys.stdin = open('input.txt')

def search(cur, total):
    global result
    if cur >= 12:
        result = min(result, total)
        return
    if total >= result:
        return

    search(cur + 1, total + min(arr[cur]*day, month))
    search(cur + 3, total + quarter)
    pass

T = int(input())

for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())

    arr = list(map(int, input().split()))
    result = float('inf')
    search(0, 0)
    print('#{} {}' .format(tc, min(result, year)))