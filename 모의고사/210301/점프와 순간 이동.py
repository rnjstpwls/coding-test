def solution(n):
    cnt = 0
    while n:
        if n % 2:
            cnt += 1
            n -= 1
        n //= 2
    return cnt


print(solution(5))
print(solution(6))
print(solution(5000))