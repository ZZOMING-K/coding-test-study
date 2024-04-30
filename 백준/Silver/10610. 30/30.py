N = input()
N = sorted(N , reverse = True)

num_sum = sum([int(i) for i in N])

if (num_sum % 3 != 0) or ('0' not in N) :
    result = -1 
else: 
    result = "".join(N)
print(result)