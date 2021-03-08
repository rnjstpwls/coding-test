import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

E, EM, M ,MH, H = map(int, input().split())

result = min(E, M ,H)
E -= result
M -= result
H -= result


while True:
    if E:
        E -= 1
    elif EM:
        EM -= 1
    else:
        break

    if M:
        M -= 1
    elif EM and EM >= MH:
        EM -= 1
    elif MH:
        MH -= 1
    else:
        break

    if H:
        H -= 1
    elif MH:
        MH -= 1
    else:
        break

    result += 1

print(result)