def solution(myString, pat):
    a = 0
    cnt = 0
    
    while True:
        idx = myString.find(pat, a)
        if idx == -1:
            break
        cnt += 1
        a = idx + 1
    
    return cnt