N = int(input()) 
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

count = 0

for i in range(len(a_list)) :
    if a_list[i] > b_list[i] : 
        count+= a_list[i] - b_list[i]

print(count)