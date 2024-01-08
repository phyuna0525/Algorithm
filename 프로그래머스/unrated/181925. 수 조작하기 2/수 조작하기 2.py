def solution(numLog):
    answer = []
    num = 0

    for i in range(len(numLog)):
        diff = numLog[i] - num

        if diff == 1:
            answer.append("w")
        elif diff == -1:
            answer.append("s")
        elif diff == 10:
            answer.append("d")
        elif diff == -10:
            answer.append("a")

        num = numLog[i]

    return ''.join(answer)
