S = input()

counter = 0
for i in range(len(S)):
    if S[i] == 'v':
        counter += 1
    else:
        counter += 2

print(counter)
