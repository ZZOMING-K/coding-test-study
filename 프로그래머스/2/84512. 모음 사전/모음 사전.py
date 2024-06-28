from itertools import product 

def solution(word):
    
    vowel = ['A','E','I','O','U']
    
    arr = []
    
    for i in range(1,6) :
        for p in product(vowel , repeat = i) :
            arr.append(''.join(p))
            
    arr.sort()
    
    for i in range(0 , len(arr)) :
        if word == arr[i] :
            answer = i+1
            
    return answer