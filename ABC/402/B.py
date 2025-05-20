from collections import deque

Q = int(input())

que = deque()

for _ in range(Q):
    In = tuple(map(int, input().split()))
    
    if In[0]==1 :
        X = In[1]
        que.append(X)
    else :
        print(que.popleft())
        