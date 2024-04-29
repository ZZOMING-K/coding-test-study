N , L = map(int, input().split()) 
height = list(map(int,input().split())) 

#과일 높이 오름차순으로 정렬 
height = sorted(height)


for h in height : 
    if L >= h : #만일 과일 높이가 스네이크버드 길이보다 작다면 길이 +1
        L = L + 1 

print(L)