import heapq

def solution(n, works):
    heap = list(map(lambda x: -x, works))
    heapq.heapify(heap)
    for _ in range(n):
        if heap:
            num = heapq.heappop(heap)
            if num != -1:
                heapq.heappush(heap, num+1)
        else:
            break


    answer = 0
    for h in heap:
        answer += (h*h)
    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))