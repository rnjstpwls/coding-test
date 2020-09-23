import sys
sys.stdin = open('input.txt')
# 동쪽1 서쪽2 남쪽3 북쪽4
K = int(sys.stdin.readline())
check = [[] for _ in range(5)]
num = []
for _ in range(6):
    direction, value = map(int, sys.stdin.readline().split())
    check[direction].append(value)
    num.append(value)

side = []

for i in range(1,5):
    if len(check[i]) == 1:
        side.append(num.index(check[i][0]))

a, b = side[0], side[1]
c, d = (a+3)%6, (b+3)%6

print(K*(num[a]*num[b] - num[c]*num[d]))


