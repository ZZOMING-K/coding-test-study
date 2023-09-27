import sys
n = int(input())


stack = []

for i in range(n) :
    p = sys.stdin.readline().split()
    if p[0] == "push"  :
        x = int(p[1])
        stack.append(x) 
    elif p[0] == "pop": 
        if len(stack) :
            print(stack.pop())
        else :
            print(-1)
    elif p[0] == "size":
        print(len(stack))
    elif p[0] == "empty" :
        if len(stack) :
            print(0)
        else :
            print(1)
    elif p[0] == "top" : 
        if len(stack) :
            print(stack[-1])
        else: 
            print(-1)