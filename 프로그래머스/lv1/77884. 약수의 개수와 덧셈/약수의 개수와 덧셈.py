def solution(left, right):
    
    answer = 0
    
    #범위가 left부터 rigt까지 
    for i in range(left , right+1) :
        result = []
        for j in range(1,i+1) :
            if i % j  == 0 :
                result.append(i)
                
        #만일 약수의 개수가 짝수라면         
        if len(result) % 2 == 0  :
            answer += i 
        else :
            answer -= i 
            
    return answer