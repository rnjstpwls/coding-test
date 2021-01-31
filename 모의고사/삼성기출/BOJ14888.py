import sys

def search(val, idx, plus, minus, mul, div):
    global maxV, minV
    if idx == N:
        maxV = max(maxV, val)
        minV = min(minV, val)
        return
    if plus:
        search(val+A[idx], idx+1, plus-1, minus, mul, div)
    if minus:
        search(val-A[idx], idx+1, plus, minus-1, mul, div)
    if mul:
        search(val*A[idx], idx+1, plus, minus, mul-1, div)
    if div:
        search(val//A[idx] if val >= 0 else -(-val//A[idx]), idx+1, plus, minus, mul, div-1)


    pass

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
plus, minus, mul, div = list(map(int, input().split()))
maxV, minV = -sys.maxsize, sys.maxsize
search(A[0], 1, plus, minus, mul, div)
print(maxV)
print(minV)