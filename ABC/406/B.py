N, K = map(int, input().split())
A = list(map(int, input().split()))

x = 1
for a in (A):
    x *= a
    l = len(str(x))
    if l > K :
        x = 1
        
print(x)
