def solution(n):
    def hanoi(n, start, mid, end):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n-1, start, end, mid)
            answer.append([start, end])
            hanoi(n-1, mid, start, end)

    answer = []
    hanoi(n, 1, 2, 3)
    return answer