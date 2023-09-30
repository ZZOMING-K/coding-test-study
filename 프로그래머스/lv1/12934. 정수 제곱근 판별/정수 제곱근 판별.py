def solution(n):
    for i in range(n+1) :
        if i ** 2 == n :
            answer = (i+1) ** 2
            break
        else :
            answer = -1
    return answer