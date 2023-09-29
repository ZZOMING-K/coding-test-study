n = int(input())
arr = []
for i in range(n) :
    name , *scores = input().split()
    arr.append((name,*map(int,scores)))

arr= sorted(arr,key = lambda x :( -x[1] , x[2] , -x[3] , x[0]))
for a in arr :
    print(a[0])