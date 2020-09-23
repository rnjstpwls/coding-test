import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

line = []
for i in range(N):
    line.insert(i-num[i],i+1)
print(*line)