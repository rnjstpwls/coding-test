# 효율성 : 시간초과

def solution(info, query):
    appliers = []
    for i in info:
        appliers.append(i.split(' '))

    answer = []


    for q in query:
        command = q.split(' ')
        command = [command[0], command[2], command[4], command[6], command[7]]
        cnt = 0
        for apply in appliers:
            if int(apply[4]) >= int(command[4]):
                if apply[0] == command[0] or command[0] == '-':
                    if apply[1] == command[1] or command[1] == '-':
                        if apply[2] == command[2] or command[2] == '-':
                            if apply[3] == command[3] or command[3] == '-':
                                cnt += 1
        answer.append(cnt)


    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))