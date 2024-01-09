def solution(num_list):
    a = sum(num_list[0::2])  # 홀수 번째 원소들의 합
    b = sum(num_list[1::2])  # 짝수 번째 원소들의 합
    
    if a >= b:
        return a
    else:
        return b
    return answer