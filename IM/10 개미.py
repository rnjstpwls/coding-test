import sys
sys.stdin = open('input.txt')

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
x, y = 1, 1
tx = t % (2*w)
ty = t % (2*h)

time = 0
while True:
    if tx == 0:
        break
    time += 1
    p += x
    if not (0 <= p <= w):
        p -= x
        x *= -1
        p += x

    if time == tx:
        break
time = 0
while True:
    if ty == 0:
        break
    time += 1

    q += y
    if not (0 <= q <= h):
        q -= y
        y *= -1
        q += y
    if time == ty:
        break
print(p, q)
