def solution(arr, intervals):
    a, c = intervals[0]
    b, d = intervals[1]
    return arr[a:c+1] + arr[b:d+1]