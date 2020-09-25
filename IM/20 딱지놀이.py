import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    player1 = []
    player2 = []
    cnt, *a = map(int ,input().split())
    cnt, *b = map(int, input().split())
    # print(a, b)
    for i in range(4,0,-1):
        player1.append(a.count(i))
        player2.append(b.count(i))
    for i in range(4):
        if player1[i] > player2[i]:
            print('A')
            break
        elif player1[i] < player2[i]:
            print('B')
            break
    else:
        print('D')
