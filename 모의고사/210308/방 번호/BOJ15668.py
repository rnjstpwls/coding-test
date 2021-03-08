import sys


def search(number):
    if number > min(N//2, 87654):
        return

    if check(N - number):
        print(number, '+', N-number)
        exit()



    for i in range(10):
        if not visited[i]:
            visited[i] = True
            search(number*10+i)
            visited[i] = False


def check(val):
    cur_visit = [False] * 10
    while val:
        if visited[val % 10] or cur_visit[val % 10]:
            return False
        cur_visit[val % 10] = True
        val //= 10
    return True

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
visited = [False] * 10
for i in range(1, 10):
    visited[i] = True
    search(i)
    visited[i] = False
print(-1)