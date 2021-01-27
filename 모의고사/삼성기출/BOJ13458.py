import sys
import math

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
A = list(map(lambda x: math.ceil(max(x-B, 0)/C), A))
print(sum(A)+N)
