T = list(str(input()))
U = list(str(input()))

ans = False
for i in range(len(T)-len(U)+1):
    sub = True
    for j in range(len(U)):
        sub &= T[i+j]=='?' or T[i+j]==U[j]
        
    ans |= sub
    
print("Yes" if ans else "No")
