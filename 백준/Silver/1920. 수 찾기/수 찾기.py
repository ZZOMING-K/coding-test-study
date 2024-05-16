N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split())) 

n_list.sort()

start  , end = 0 , len(n_list)-1 

def bisect(arr , target , start , end) : 

    while start <= end :
        mid = (start+end) //2 
        if arr[mid] == target :
            return 1 
        elif arr[mid] > target :
            end = mid -1 
        else :
            start = mid+1 
    return 0 
        
for i in m_list :
    print(bisect(n_list , i , start , end))