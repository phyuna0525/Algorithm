def solution(my_string, index_list):
    answer = ""
    for index in index_list:
        if 0 <= index < len(my_string):
            answer += my_string[index]

    return answer
