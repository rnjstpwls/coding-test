import sys
sys.stdin = open('input.txt')

for tc in range(4):
    x1, y1, x4, y4, p1, q1, p4, q4 = map(int, sys.stdin.readline().split())
    x2, y2, x3, y3 = x4, y1, x1, y4
    p2, q2, p3, q3 = p4, q1, p1, q4

    if (x1, y1) == (p4, q4) or (x4, y4) == (p1, q1) or (x2, y2) == (p3, q3) or (x3, y3) == (p2, q2):
        print('c')
        continue

    if x2 < p1 or p2 < x1 or y1 > q3 or q1 > y3:
        print('d')
        continue

    if x2 == p1 or p2 == x1 or y1 == q3 or q1 == y3:
        print('b')
        continue
    print('a')