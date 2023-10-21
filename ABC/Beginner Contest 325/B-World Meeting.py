N = int(input())
spot = []

for _ in range(N):
    W, X = map(int, input().split())
    spot.append((W, X))

ans = 0
for W, X in spot:
    base = X
    for start_time in range(9, 17):
        cnt = 0
        for w, x in spot:
            if base - x < 0:  # 基準より遅い
                if 9 <= (start_time - abs(base - x)) % 24 <= 17:
                    cnt += w
            else:  # 基準より早い
                if 9 <= (start_time + abs(base - x)) % 24 <= 17:
                    cnt += w
        ans = max(ans, cnt)

print(ans)
