S = list(str(input()))

char = 'a'
while char in S:
    char = chr(ord(char)+1)
    
print(char)
