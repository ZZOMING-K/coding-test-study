def solution(answers):
    
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    
    for i in range(len(answers)) :
        #5개의 답이 반복되므로 
        if answers[i] == pattern1[ i % len(pattern1) ] :
            score[0] += 1 
        if answers[i] == pattern2[ i % len(pattern2)] :
            score[1] += 1 
        if answers[i] == pattern3[ i % len(pattern3)] :
            score[2] += 1
    
    result = []
    for idx , s in enumerate(score) :
        if s == max(score) :
            result.append(idx+1)
    
    return result