N, M = map(int, input().split())
A = list(map(int, input().split()))

X = set()

for i, a in enumerate(A):
    X.add(a)
        
    if len(X)==M :
        print(N-i)
        break
    
    if i==N-1 :
        print(0)
    