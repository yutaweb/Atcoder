# X = input()
# M = int(input())
# Max = int(max(list(X)))
# count = 0
# ans = 0
# flag = True
# expo = Max + 1
# reverse = X[::-1]
# while flag:
#     for i, x in enumerate(reverse):
#         box = int(x)*(expo**i)
#         ans += box
#     if ans <= M:
#         count += 1
#         expo += 1
#         ans = 0
#     else:
#         flag = False
#
#
# print(count)
# 参考URL：https://marco-note.net/abc-192-work-log/


def solve(m):
    global X, M
    base = 1
    num = 0
    for x in X:
        num += x * base
        if num > M:
            return False
        base *= m
    return True


X = list(map(int, list(input())))
X.reverse()  # 逆順にしておくと、桁とindexが一致するため便利
M = int(input())
d = max(X)

if len(X) == 1:  # Xが1桁のときは答えは0 or 1
    print(1 if d <= M else 0)
    exit()

# 二分探索を使ってnの最大値を求める
ok = 0  # 下限を0にすることがポイント
ng = pow(10, 18) + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(max(0, ok - d))