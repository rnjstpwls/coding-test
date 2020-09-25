N = int(input())

table = [[0]*101 for _ in range(101)]

for i in range(1, N+1):
    x, y, l, h = map(int, input().split())

    for j in range(h):
        for k in range(l):
            table[y+j][x+k] = i
for i in range(1, N+1):
    cnt = 0
    for t in table:
        cnt += t.count(i)
    print(cnt)