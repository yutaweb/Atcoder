N, K = map(int, input().split())

H = []
for _ in range(N):
    H.append(int(input()))

H.sort()

diff = []

for i in range(N - K + 1):
    diff.append(H[i + K - 1] - H[i])

print(min(diff))
