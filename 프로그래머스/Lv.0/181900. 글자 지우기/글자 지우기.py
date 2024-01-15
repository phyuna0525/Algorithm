def solution(my_string, indices):
    my_list = list(my_string)

    indices.sort(reverse=True)

    for i in indices:
        if 0 <= i < len(my_list):
            del my_list[i]
    answer = ''.join(my_list)
    return answer
