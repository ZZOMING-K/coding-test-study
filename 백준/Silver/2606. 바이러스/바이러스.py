n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    
def recur(node) :
    visited[node] = 1
    for nxt in arr[node] :
        if visited[nxt] ==1 :
            continue
        recur(nxt)
recur(1)       
print(sum(visited)-1)