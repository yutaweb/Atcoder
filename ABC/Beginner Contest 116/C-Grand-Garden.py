# 数学で解く
N = int(input())
H = list(map(int, input().split()))
H.append(0)  # 最後の数値を数える為

ans = 0
for i in range(len(H)-1):
    diff = H[i] - H[i+1]
    if diff > 0:
        ans += diff

print(ans)
