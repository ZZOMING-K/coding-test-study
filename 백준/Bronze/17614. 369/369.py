n = int(input())
check = '369'
cnt = 0
for i in range(1,n+1) :
    str_num = str(i)
    for c in check :
        cnt += str_num.count(c)
        
print(cnt)
            