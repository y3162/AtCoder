N = int(input())
A = list(map(int, input().split()))

S = (sum(A)**2 - sum(map(lambda x: x**2, A))) // 2
print(S)
