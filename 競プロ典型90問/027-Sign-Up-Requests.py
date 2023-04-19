N = int(input())
User = []
Index = []

for i in range(N):
    S = input()
    if S not in User:
        User.append(S)
        Index.append(i+1)

print(*Index, sep='\n')
