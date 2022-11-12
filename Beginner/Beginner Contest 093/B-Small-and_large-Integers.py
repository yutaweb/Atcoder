A, B, K = map(int, input().split())

min_range = A + K - 1
max_range = B - K + 1

if min_range >= max_range:
    for v in range(A, B + 1):
        print(v)
else:
    for v in range(A, min_range + 1):
        print(v)
    for v in range(max_range, B + 1):
        print(v)

