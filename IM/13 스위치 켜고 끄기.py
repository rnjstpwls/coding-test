import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
sw = list(map(int, sys.stdin.readline().split()))

students = int(sys.stdin.readline())

for _ in range(students):
    gender, value = map(int, sys.stdin.readline().split())

    if gender == 1:
        for i in range(1, N//value+1):
            sw[value*i - 1] = 1 - sw[value*i - 1]
        pass
    else:
        sw[value-1] = 1 - sw[value-1]
        idx = 1
        while True:
            if N < (value+idx) or (value-idx) < 1 or sw[value+idx-1] != sw[value-idx-1]:
                break
            sw[value+idx-1] = 1 - sw[value+idx-1]
            sw[value-idx-1] = 1 - sw[value-idx-1]
            idx += 1
        pass

for i in range(len(sw)):
    if i%20==0 and i!=0:
        print()
    print(sw[i],end=' ')
