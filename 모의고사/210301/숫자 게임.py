import heapq

def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    while A and B:
        if A[0] < B[0]:
            heapq.heappop(A)
            heapq.heappop(B)
            answer += 1
        else:
            heapq.heappop(B)
    return answer

A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A, B))
A = [2,2,2,2]
B = [1,1,1,1]
print(solution(A, B))
