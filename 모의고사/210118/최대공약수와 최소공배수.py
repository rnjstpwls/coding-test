def solution(n, m):

    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    lcm = (n // gcd) * m
    answer = [gcd, lcm]
    return answer