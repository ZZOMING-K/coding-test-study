

def solution(n):
    #n이 짝수 일 경우
    if n % 2 == 0 :
        answer = '수박'*(n//2)
    else :
        answer = '수'+('박수')*(n//2)
        
    return answer