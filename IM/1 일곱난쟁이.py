import sys
sys.stdin = open('input.txt')

def search():
    for i in range(8):
        for j in range(i + 1, 9):
            if tall[i] + tall[j] == find_value:
                return (i, j)


tall = [int(sys.stdin.readline()) for _ in range(9)]

find_value = sum(tall) - 100

a, b = search()
result = []
for i in range(9):
    if i == a or i == b:
        continue
    result.append(tall[i])
result.sort()
for i in range(7):
    print(result[i], end='\n')
