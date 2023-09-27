import sys

n = int(input())
arr = [int(sys.stdin.readline()) for i in range(n)]
arr = reversed(arr)

max_bar = 0
cnt = 0

for i in arr :
    if max_bar < i :
        max_bar = i
        cnt += 1 
print(cnt)