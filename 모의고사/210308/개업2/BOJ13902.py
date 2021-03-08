import sys

input = sys.stdin.readline

N, M = map(int, input().split())
wok = list(map(int, input().split()))
MAX = 9876543210
dp = [MAX] * (N+1)
dp[0] = 0
possible = wok.copy()
for i in range(M-1):
    for j in range(i+1, M):
        possible.append(wok[i]+wok[j])

for p in set(possible):
    for i in range(N-p+1):
        dp[i+p] = min(dp[i+p], dp[i] + 1)
print(dp[-1] if dp[-1] != MAX else -1)