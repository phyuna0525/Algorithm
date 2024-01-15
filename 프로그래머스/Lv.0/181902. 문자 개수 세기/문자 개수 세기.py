def solution(my_string):
    answer = [0 for i in range(52)]
    for a in my_string:
        if a.isupper(): k = 65
        else: k = 71
        answer[ord(a)-k] += 1
    return answer