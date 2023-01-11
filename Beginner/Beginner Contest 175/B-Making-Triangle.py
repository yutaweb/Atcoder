N = int(input())
L = list(map(int, input().split()))

counter = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (L[i] == L[j]) or (L[i] == L[k]) or (L[j] == L[k]):
                continue
            if (L[i] >= (L[j] + L[k])) or ((L[i] + L[j]) <= L[k]) or ((L[i] + L[k]) <= L[j]):
                continue
            
            counter += 1

print(counter)
