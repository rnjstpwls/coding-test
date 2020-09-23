import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
paper = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

white_board = [[0]*100 for _ in range(100)]

while paper:
    x, y = paper.pop()
    for i in range(10):
        for j in range(10):
            white_board[y+i][x+j] = 1
result = 0
for i in range(100):
    result += sum(white_board[i])
print(result)