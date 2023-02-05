S = input()

counter = 0

i = 0
j = len(S) - 1
while i < j:
    if S[i] != S[len(S) - i - 1]:
        counter += 1

    i += 1
    j -= 1

print(counter)
