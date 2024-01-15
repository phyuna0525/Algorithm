def solution(n, k):
    answer = []
    for i in range(n):
        if (i+1)*k > n:
            return answer
        answer.append((i+1)*k)
    return answer