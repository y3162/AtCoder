N = int(input())
P = list(map(int, input().split()))

inc = []
i = 0
while i<N-1 :
    count = 1
    while i<N-1 and P[i] < P[i+1]:
        count += 1
        i += 1
    if count>0 :
        inc.append(count)
        
    while i<N-1 and P[i] > P[i+1]:
        i += 1
        
    if i==N-1 :
        break

res = 0  
for i in range(len(inc)-1):
    res += (inc[i]-1) * (inc[i+1]-1) 
    
print(res)
