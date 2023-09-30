def solution(num):
    cnt = 0
    result = 0
    
    while num > 1 :
        if num % 2 == 0 :
            num=num //2 
        else :
            num = num * 3 + 1
        cnt += 1 
        result += 1 
        
    if cnt >= 500 :
        result = -1
    
    return result