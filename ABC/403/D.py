N, D = map(int, input().split())
A = list(map(int, input().split()))

num = [0]*(max(A)+1)
for a in A:
    num[a] += 1

B = 0
if D==0 :
    for n in num:
        B += not n==0
else :
    for i in range(min(D, len(num))):
        X = [num[j] for j in range(i, len(num), D)]

        dp = [0]*len(X)
        dp[0] = X[0]
        if len(X)>1 :
            dp[1] = max(X[0], X[1])
        for j in range(2, len(X), 1):
            dp[j] = max(dp[j-1], dp[j-2]+X[j])

        B += dp[len(X)-1]
    
print(N-B)
