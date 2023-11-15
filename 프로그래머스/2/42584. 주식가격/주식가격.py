def solution(prices):
    
    answer = [0] * len(prices)
    stack = [] 
    
    for idx , price in enumerate(prices) :
        
        while stack and price < prices[stack[-1]] :
            last = stack.pop()
            answer[last] = idx - last
        
        stack.append(idx)
        
        if answer[idx] == 0 :
            answer[idx] = len(prices) - idx -1
        
    return answer