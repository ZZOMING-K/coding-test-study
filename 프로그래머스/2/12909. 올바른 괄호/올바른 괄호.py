def solution(s):
    
    stack = []

    for char in s :
        
        if char =='(':
            stack.append(char)
        
        elif not stack or stack.pop() != '(' :
            return False
            
    return len(stack) == 0 