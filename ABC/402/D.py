N, M = map(int, input().split())

same = [0]*N

for _ in range(M):
    A, B = map(int, input().split())
    same[(A+B-2)%N] += 1
    
def nCr(n, r):
    if n < r :
        return 0
    elif r > n-r :
        r = n-r
        
    res = 1
    for i in range(n, n-r, -1):
        res *= i
    for i in range(1, r+1, 1):
        res //= i
        
    return res

ans = nCr(M, 2)
for s in same:
    ans -= nCr(s, 2)
    
print(ans)
