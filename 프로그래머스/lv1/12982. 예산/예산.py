def solution(d, budget):
    #오름차순정렬 
    d = sorted(d)
    #신청금액보다 클 경우 가장 큰 금액부터 반환 
    #pop은 맨마지막 원소를 리턴하여 해당 원소 삭제 
    while budget < sum(d) :
        d.pop()    
    return len(d)

