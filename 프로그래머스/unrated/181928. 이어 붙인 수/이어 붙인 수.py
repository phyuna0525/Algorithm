def solution(num_list):
    answer = ''
    answer1 = ''
    a = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            answer += str(num_list[i])
        else:
            answer1 += str(num_list[i])
    a = int(answer) + int(answer1)
    return a
