import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

tmp = list(map(int, sys.stdin.readline().split()))
tmp_sum = [0, tmp[0]]
for i in range(1, N):
    tmp_sum.append(tmp_sum[-1]+tmp[i])
# print(tmp_sum)
result = -200 * 100000
# print(result)
for i in range(N-K+1):
    if tmp_sum[i+K]-tmp_sum[i] > result:
        result = tmp_sum[i+K]-tmp_sum[i]
print(result)