A, B, C, D = map(int, input().split())

deadline = A*60 + B
submission = C*60 + D

if submission < deadline :
    print("Yes")
else :
    print("No")
