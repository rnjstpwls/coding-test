def solution(arr):
    def recursion(arr):
        N = len(arr)
        half = N // 2
        if check(arr):
            result[arr[0][0]] += 1
            return

        LT = []
        RT = []
        LB = []
        RB = []
        for r in range(half):
            LT.append(arr[r][:half])
            RT.append(arr[r][half:])
        for r in range(half, N):
            LB.append(arr[r][:half])
            RB.append(arr[r][half:])
        recursion(LT)
        recursion(RT)
        recursion(LB)
        recursion(RB)


    result = [0, 0]

    def check(arr):
        tmp = arr[0][0]
        for r in range(len(arr)):
            for c in range(len(arr)):
                if tmp != arr[r][c]:
                    return False
        return True

    recursion(arr)

    return result
