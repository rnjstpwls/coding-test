def solution(new_id):
    step1 = str()
    available = {'-', '_', '.',
                 '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                 'w', 'x', 'y', 'z'}
    for c in new_id:
        if ord('A') <= ord(c) <= ord('Z'):
            step1 += chr(ord(c)+32)
        elif c in available:
            step1 += c

    while True:
        if '..' in step1:
            step1 = step1.replace('..', '.')
        else:
            break

    step1 = step1.strip('.')
    if not step1:
        step1 = 'a'
    else:
        step1 = step1[:15].rstrip('.')
    if len(step1) == 2:
        step1 += step1[-1]
    elif len(step1) == 1:
        step1 += step1[-1]
        step1 += step1[-1]
    answer = step1
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
