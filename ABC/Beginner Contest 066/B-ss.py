S = list(input())

for i in range(len(S)):
    S.pop(len(S) - 1)
    if len(S) % 2 == 0:
        if S[0:len(S)//2] == S[len(S)//2:]:
            exit(print(len(S)))

