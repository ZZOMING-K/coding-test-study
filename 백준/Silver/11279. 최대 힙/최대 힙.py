import sys
import heapq

n = int(input())
arr = []
for _ in range(n) :
    i = int(sys.stdin.readline())
    if i > 0 :
        heapq.heappush(arr,-i)
    elif i == 0 :
        if len(arr) == 0 :
            print(0)
        else:    
            print(-1*heapq.heappop(arr)) 