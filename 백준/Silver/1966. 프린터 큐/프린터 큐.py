from collections import deque

def find_count() : 
    N , M = map(int,input().split())
    num_list = deque(list(map(int,input().split())))


    new_list = deque()
    for idx,num in enumerate(num_list) :
        new_list.append((idx , num)) 

    count = 0     

    while len(new_list) > 0 :
    
        max_num = max(new_list , key = lambda x : x[1])[1]
        
        x = new_list.popleft()
    
        if x[1] == max_num : 
            count+=1
        
            if x[0] == M : 
                return count 
                break
        
            continue
    
        new_list.append(x) 

T = int(input())
for _ in range(T):
    answer = find_count()
    print(answer)