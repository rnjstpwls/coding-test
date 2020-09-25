import sys
sys.stdin = open('input.txt')

def search(value):
    if value == 0 or value == 5:
        return 5 - value
    if value == 1 or value == 3:
        return 4 - value
    if value == 2 or value == 4:
        return 6 - value

N = int(sys.stdin.readline())
dice = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
for i in range(6):
    tmp = 0
    bottom = dice[0][i]
    opposite = dice[0][search(i)]
    if bottom != 6 and opposite != 6:
        tmp += 6
    elif bottom != 5 and opposite != 5:
        tmp += 5
    else:
        tmp += 4
    for j in range(1, N):
        bottom = opposite
        opposite = dice[j][search(dice[j].index(bottom))]
        if bottom != 6 and opposite != 6:
            tmp += 6
        elif bottom != 5 and opposite != 5:
            tmp += 5
        else:
            tmp += 4
    if result < tmp:
        result = tmp

print(result)