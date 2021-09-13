N, X = map(int, input().split())
S = 0

for i in range(N):
    V, P = map(int, input().split())
    S += V*P
    if S > X*100:
        print(i+1)
        exit()

print(-1)