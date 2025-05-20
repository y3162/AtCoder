N, M = map(int, input().split())

E = [set() for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    E[A-1].add(B-1)
    E[B-1].add(A-1)
    
is_cycle = M==N
for i in range(N):
    is_cycle &= len(E[i])==2

if is_cycle : 
    connected = [False]*N
    start, end = 0, E[0].pop()
    E[end].remove(0)
    count = 1
    
    while E[end] :
        start = end
        end = E[end].pop()
        E[end].remove(start)
        count += 1
        
    is_cycle &= end==0 and count==M

print("Yes" if is_cycle else "No")
