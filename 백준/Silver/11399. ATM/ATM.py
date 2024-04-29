N = int(input())
P_list = list(map(int,input().split())) 

#시간 오름차순 정렬 
P_list = sorted(P_list) 

time = 0 
sum_time = 0 

for p in P_list : 
    time += p 
    sum_time += time 

print(sum_time)
