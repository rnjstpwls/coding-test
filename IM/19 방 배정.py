import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
male = [0] * 7
female = [0] * 7

room = 0
for _ in range(N):
    gender, grade = map(int, input().split())
    if gender == 0:
        female[grade] += 1
        if female[grade] == K:
            female[grade] = 0
            room += 1
    else:
        male[grade] += 1
        if male[grade] == K:
            male[grade] = 0
            room += 1
empty_room = 0
for i in range(1, 7):
    if male[i] == 0:
        empty_room += 1
    if female[i] == 0:
        empty_room += 1

print(room+12-empty_room)