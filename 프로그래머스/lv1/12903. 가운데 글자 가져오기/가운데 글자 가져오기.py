def solution(s):
    st = len(s)//2
    if len(s) % 2 == 1 :
        answer = s[st]
    else :
        answer = s[st-1:st+1]
    return answer