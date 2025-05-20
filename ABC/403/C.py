N, M, Q = map(int, input().split())

view = [set() for _ in range(N)]
full = [False]*N

for _ in range(Q):
    In = tuple(map(int, input().split()))
    if In[0]==1 :
        X, Y = In[1], In[2]
        view[X-1].add(Y-1)
    elif In[0]==2 :
        X = In[1]
        full[X-1] = True
    else :
        X, Y = In[1], In[2]
        print("Yes" if full[X-1] or Y-1 in view[X-1] else "No")
        