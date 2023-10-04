n = int(input())
profit = [list(map(int,input().split())) for _ in range(n)]

def recur(idx,p) : 
    global answer

    #만일 근무일이 퇴사일을 넘어서는 경우는 제외 
    if idx >= n:
        if idx > n :
            return              
        result = p     
        answer = max(answer, result)
        return answer 

    #해당 요일에 상담을 하는 경우 
    recur(idx + profit[idx][0], p + profit[idx][1])
    #해당요일에 상담을 하지 않는 경우
    recur(idx+1 , p ) 



answer = 0 
recur(0,0)
print(answer)