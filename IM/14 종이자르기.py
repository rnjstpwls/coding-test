import sys
sys.stdin = open('input.txt')

width, height = map(int,sys.stdin.readline().split())
garo = [0,width]
sero = [0,height]
N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    if a == 0:
        sero.append(b)
    else:
        garo.append(b)
garo.sort()
sero.sort()

garo_length = []
sero_length = []

for i in range(len(garo)-1):
    garo_length.append(garo[i+1]-garo[i])
for i in range(len(sero)-1):
    sero_length.append(sero[i+1]-sero[i])



result = 0
for g in garo_length:
    for s in sero_length:
        if g*s > result:
            result = g*s
print(result)