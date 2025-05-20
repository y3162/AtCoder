N, M = map(int, input().split())
C = list(map(int, input().split()))
A = [list(map(int, input().split()))[1:] for _ in range(M)]
Z = [[z+1 in A[a] for a in range(M)] for z in range(N)]

res = 2*N*10**9 + 1

for bit in range(3**N):
    cost = 0
    n_visit = [0]*N
    watched = [0]*M
    x = bit
    for z in range(N):
        n_visit[z] = x%3
        cost += C[z] * n_visit[z]
        for a in range(M):
            if Z[z][a] :
                watched[a] += n_visit[z]
        
        x //= 3
       
    see_tiwce_or_more = True
    for a in range(M):
        if watched[a]<2 :
            see_tiwce_or_more = False
    
    if see_tiwce_or_more :
        res = min(res, cost)
    
print(res)
