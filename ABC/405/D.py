from collections import deque

H, W = map(int, input().split())
S = [list(map(str, input())) for _ in range(H)]

que = deque()

for i, row in enumerate(S):
    for j, s in enumerate(row):
        if s=='E':
            que.append((i, j))

while que:
    i, j = que.popleft()
    
    r, c = i-1, j
    if 0<=r and r<H and 0<=c and c<W and S[r][c]=='.':
        S[r][c] = 'v'
        que.append((r, c))
    
    r, c = i+1, j
    if 0<=r and r<H and 0<=c and c<W and S[r][c]=='.':
        S[r][c] = '^'
        que.append((r, c))
        
    r, c = i, j-1
    if 0<=r and r<H and 0<=c and c<W and S[r][c]=='.':
        S[r][c] = '>'
        que.append((r, c))
        
    r, c = i, j+1
    if 0<=r and r<H and 0<=c and c<W and S[r][c]=='.':
        S[r][c] = '<'
        que.append((r, c))
        
for i in range(H):
    print("".join(S[i]))
        