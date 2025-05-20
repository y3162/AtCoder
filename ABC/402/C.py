N, M = map(int, input().split())

A = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
B = list(map(int, input().split()))

in_recipe = [set() for _ in range(N)]
for d in range(M):
    for a in A[d]:
        in_recipe[a-1].add(d+1)

cannot_eat = set([d+1 for d in range(M)])

for b in B:
    for d in in_recipe[b-1] :
        A[d-1].remove(b)
        if not A[d-1] :
            cannot_eat.remove(d)
        
    in_recipe[b-1] = set()
    
    print(M-len(cannot_eat))
