N = int(input())

S = [list(str(input())) for _ in range(N)]
T = [list(str(input())) for _ in range(N)]

def n_operations():
    count = 0
    for i in range(N):
        for j in range(N):
            if not S[i][j]==T[i][j] :
                count += 1
                
    return count

def rorate_right_90():
    X = [['?']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            X[i][j] = S[N-1-j][i]
            
    return X

ans = N**2
for i in range(4):
    ans = min(ans, i+n_operations())
    S = rorate_right_90()
    
print(ans)
