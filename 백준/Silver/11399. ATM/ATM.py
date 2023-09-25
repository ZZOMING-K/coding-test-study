n = int(input())
mem = list(map(int,input().split()))
#오름차순정렬
mem.sort()

time_sum = []

result = 0
for i in mem :
    result += i 
    time_sum.append(result)

print(sum(time_sum))
    
    