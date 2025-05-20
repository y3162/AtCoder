N = int(input())
A = list(map(int, input().split()))

S = 0
for i in range(0, N, 2):
    S += A[i]
    
print(S)
