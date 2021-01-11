def solution(numbers):
    length = len(numbers)
    result = set()
    for i in range(length-1):
        for j in range(i+1, length):
            result.add(numbers[i]+numbers[j])
    return sorted(list(result))

print(solution([1, 2, 3, 4, 5]))