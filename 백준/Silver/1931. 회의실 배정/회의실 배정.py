import sys

n = int(input())

end_point = 0
result = 0 

arr = []

for i in range(0,n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))

for new_start, new_end in arr:
    if end_point <= new_start:
        result += 1
        end_point = new_end

print(result)