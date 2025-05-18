H, W, N = map(int, input().split())

R = [set() for _ in range(H)]
C = [set() for _ in range(W)]
for _ in range(N):
    X, Y = map(int, input().split())
    R[X-1].add(Y-1)
    C[Y-1].add(X-1)
    
Q = int(input())
res = []
for _ in range(Q):
    t, v = map(int, input().split())
    if t==1 :
        x = v-1
        res.append(len(R[x]))
        for y in R[x]:
            C[y].remove(x)
        R[x].clear()
    
    if t==2 :
        y = v-1
        res.append(len(C[y]))
        for x in C[y]:
            R[x].remove(y)
        C[y].clear()
       
for r in res:
    print(r)
     