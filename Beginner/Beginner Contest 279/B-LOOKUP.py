S = input()
T = input()

window_size = len(T)
for i in range(len(S) - window_size + 1):
    if S[i:i + window_size] == T:
        print('Yes')
        exit()

print('No')
