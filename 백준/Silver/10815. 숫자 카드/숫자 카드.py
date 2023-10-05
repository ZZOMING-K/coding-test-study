n = int(input())
arr1 = sorted(list(map(int,input().split())))

m = int(input())
arr2 = list(map(int,input().split()))

result=[]
for num in arr2 :
    s = 0 
    e = n-1
    flag = False

    while s <= e : #s와 e가 교차되지 않았다면

        mid = (s+e)//2

        #업인가요?다운인가요?정답인가요?

        if arr1[mid] == num :
            #정답입니다! 
            flag = True
            break

        elif arr1[mid] > num :
            e = mid - 1
        
        else :
            s = mid + 1 
    
    if flag :
        result.append(1)
    else :
        result.append(0)

print(*result)