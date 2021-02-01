def solution(s):
    def pelindrome(string):
        if string == string[::-1]:
            return True
        else:
            return False
    length = len(s)
    answer = 0
    for i in range(length):
        for j in range(i+1, length+1):

            if pelindrome(s[i:j]):
                answer = max(answer, j-i)

    return answer
solution('abacde')