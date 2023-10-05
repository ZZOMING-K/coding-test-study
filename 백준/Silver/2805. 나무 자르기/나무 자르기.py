n,m = map(int,input().split())
forest = list(map(int,input().split()))

s = 0 
e = max(forest)

while e>=s:
    
    mid = (s+e) //2
    
    wood = 0
    #가져갈 수 있는 나무 계산
    for tree in forest :
        if tree >= mid :
            wood += tree-mid
    
    if wood >= m :
        s= mid+1
    else :
        e = mid-1
        
print(e)