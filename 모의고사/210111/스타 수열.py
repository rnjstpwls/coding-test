def solution(a):
    answer = 0
    tmp = [[] for _ in range(len(a))]
    for i in range(len(a)):
        tmp[a[i]].append(i)

    for i in range(len(a)):
        if len(tmp[i]) > max(answer, 1):
            cnt = 1
            length = len(tmp[i])

            if tmp[i][0] == 0:
                isFirst = True
            else:
                isFirst = False

            for j in range(1, length):
                if isFirst:
                    if tmp[i][j] - tmp[i][j-1] == 2:
                        cnt += 1
                    elif tmp[i][j] - tmp[i][j-1] > 2:
                        cnt += 1
                        isFirst = False
                else:
                    if tmp[i][j] - tmp[i][j-1] == 1:
                        isFirst = True
                    cnt += 1

            if isFirst and tmp[i][-1] == len(a)-1:
                cnt -= 1

            answer = max(answer, cnt)


    return answer * 2