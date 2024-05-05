def solution(array):
    sort = sorted(array)
    n = len(sort)
    if n % 2 != 0:
        return sort[n // 2]
    else:
        middle1 = sort[(n // 2) - 1]
        middle2 = sort[n // 2]
        return (middle1 + middle2) / 2