def solution(n):
    arr = list(map(int,str(n)))
    arr.sort(reverse = True)
    
    arr = ''.join(map(str,arr))
    return int(arr)
    
