H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
lists = []
for i in range(H):
    lists.append(input())

ans = 1

# 上へ探索
for column in reversed(range(X)):
    if lists[column][Y] == "#":
        break
    else:
        ans += 1

# 下へ探索
for column in range(X+1, H):
    if lists[column][Y] == "#":
        break
    else:
        ans += 1

# 左へ探索
for row in reversed(range(Y)):
    if lists[X][row] == "#":
        break
    else:
        ans += 1

# 右へ探索
for row in range(Y+1, W):
    if lists[X][row] == "#":
        break
    else:
        ans += 1

print(ans)