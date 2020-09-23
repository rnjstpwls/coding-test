import sys

sys.stdin = open('input.txt')

def bingo_check():
    cnt = 0
    for i in range(5):
        if sum(check[i]) == 5:
            cnt += 1

    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += check[j][i]
        if tmp == 5:
            cnt += 1

    tmp = 0
    for i in range(5):
        tmp += check[i][i]
    if tmp == 5:
        cnt += 1

    tmp = 0
    for i in range(5):
        tmp += check[4-i][i]
    if tmp == 5:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False



bingo_board = []
for _ in range(5):
    bingo_board += list(map(int,sys.stdin.readline().split()))


announce = []
for _ in range(5):
    announce += list(map(int,sys.stdin.readline().split()))

check = [[0]*5 for _ in range(5)]
cnt = 1
while announce:
    current = announce.pop(0)
    find_value = bingo_board.index(current)
    check[find_value//5][find_value%5] = 1

    if bingo_check():
        break

    cnt += 1

print(cnt)