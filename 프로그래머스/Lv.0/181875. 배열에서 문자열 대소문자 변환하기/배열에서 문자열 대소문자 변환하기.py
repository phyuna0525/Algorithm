def solution(strArr):
    answer = []
    for idx, a in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(a.lower())
        else:
            answer.append(a.upper())
    return answer