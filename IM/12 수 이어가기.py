N = int(input())

max_length = 0
basic = [N]

for i in range(N+1):
    tmp = basic + [i]
    while True:
        current = tmp[-2] - tmp[-1]
        if current < 0:
            break
        tmp.append(current)
    if len(tmp) > max_length:
        max_length = len(tmp)
        result = tmp
print(max_length)
print(*result)
