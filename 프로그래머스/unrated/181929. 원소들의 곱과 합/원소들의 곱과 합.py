def solution(num_list):
    answer = 0
    a = 0
    b = 1
    for i in range(len(num_list)):
        a += num_list[i]
        b *= num_list[i]
    if a*a > b:
        return 1
    else: return 0