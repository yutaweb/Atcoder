N, X = map(int, input().split())
P = list(map(int, input().split()))

for i, v in enumerate(P):
    if v == X:
        print(i + 1)
        exit()
