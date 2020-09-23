import sys
sys.stdin = open('input.txt')


N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

maxv = 1
cnt = 1
for i in range(1, N):
    if num[i-1] >= num[i]:
        cnt += 1
    else:
        cnt = 1
    if maxv < cnt:
        maxv = cnt

cnt = 1
for i in range(1, N):
    if num[i-1] <= num[i]:
        cnt += 1
    else:
        cnt = 1
    if maxv < cnt:
        maxv = cnt

print(maxv)