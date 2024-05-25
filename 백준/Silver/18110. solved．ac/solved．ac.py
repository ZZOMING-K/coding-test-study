from sys import stdin


def rdup(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(stdin.readline())

if n == 0:
    print(0)

else:
    level_list = []
    
    for i in range(n):
        level_list.append(int(stdin.readline()))
        
    level_list.sort()
    no_num = rdup(n * 0.15)
    
    print(rdup(sum(level_list[no_num:n-no_num])/len(level_list[no_num:n-no_num])))