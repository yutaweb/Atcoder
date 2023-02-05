N = int(input())
S = list(input())

for i in range(1, N):  # 1 ~ N - 1
    counter = 0
    for k in range(N - i):  # 0 ~ N
        if S[k] == S[k+i]:
            break
        if S[k] != S[k+i]:
            counter += 1

    print(counter)





