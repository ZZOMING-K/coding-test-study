def solution(arr):
    answer = []
    answer.append(arr[0])
    # 이전 숫자와 동일할경우 삭제 
    for i in range(1,len(arr)) :
        if arr[i] != arr[i-1] :
            answer.append(arr[i])
    return answer