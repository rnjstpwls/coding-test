from itertools import combinations
from collections import deque
import sys


def search(s):
    visited = [False] * (N+1)
    s = list(s)
    q = deque()
    q.append(s[0])
    visited[s[0]] = True
    while q:
        current = q.popleft()
        for next in link[current]:
            if next in s and not visited[next]:
                visited[next] = True
                q.append(next)
    for i in s:
        if visited[i] == False:
            return False
    return True


N = int(input())
numbers = [0] + list(map(int, input().split()))

link = [[]]
for _ in range(N):
    cnt, *l = map(int, input().split())
    if cnt:
        link.append(l)
    else:
        link.append([])

result = sys.maxsize
total = sum(numbers)
for i in range(1, (N//2)+1):
    candidate = combinations(range(1, N+1), i)
    for c in candidate:

        c = set(c)
        opponent = set(range(1, N+1)) - c

        if search(c) and search(opponent):
            c = list(c)
            tmp = 0
            for element in c:
                tmp += numbers[element]
            result = min(result, abs(total-tmp-tmp))

if result == sys.maxsize:
    print(-1)
else:
    print(result)