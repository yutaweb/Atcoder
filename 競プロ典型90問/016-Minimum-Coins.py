N = int(input())
A, B, C = map(int, input().split())

ans = 10**9
for i in range(10000):
    for j in range(10000):
        M = A*i+B*j
        if M > N:
            break
        if not (N-M) % C:
            ans = min(ans, i+j+(N-M)//C)


print(ans)
