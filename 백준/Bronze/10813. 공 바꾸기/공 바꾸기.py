N,M = map(int,input().split())
num =[]
for n in range(1,N+1):
    num.append(n)

for m in range(M) :
    i,j = map(int,input().split())
    num[i-1] , num[j-1] = num[j-1] , num[i-1]
for i in num :
    print(i , end = " ")