import sys
from itertools import combinations

def search(point):
    arrow1, arrow2, arrow3 = point
    arrow1 = (N, arrow1)
    arrow2 = (N, arrow2)
    arrow3 = (N, arrow3)
    arrow = [arrow1, arrow2, arrow3]
    enemy_tmp = enemy.copy()
    cnt = 0

    while enemy_tmp:
        real_tmp = set()
        for p in arrow:
            tmp = [distance(p, enemy_point) for enemy_point in enemy_tmp]

            if tmp and min(tmp) <= D:
                real_tmp.add(tmp.index(min(tmp)))

        for i in real_tmp:
            enemy_tmp[i] = (-1, -1)
        cnt += len(real_tmp)

        tmp = []
        for enemy_r, enemy_c in enemy_tmp:
            if enemy_r+1 == N or (enemy_r, enemy_c) == (-1, -1):
                continue
            tmp.append((enemy_r+1, enemy_c))
        enemy_tmp = tmp
    return cnt

def distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])


def find_enemy():
    for c in range(M):
        for r in range(N-1, -1, -1):
            if arr[r][c] == 1:
                enemy.append((r, c))
    pass

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M, D = map(int, input().split())

order = list(combinations(range(M), 3))
dp = [0] * len(order)

arr = list(list(map(int, input().split())) for _ in range(N))
enemy = []

find_enemy()
result = 0
for point in order:
    result = max(search(point), result)
print(result)
