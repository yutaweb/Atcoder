A, B, C, X, Y = map(int, input().split())

# Pattern 1
if (A+B) <= 2*C:
    print(A*X + B*Y)
else:
    if X <= Y:
        print(min(C*(2*X) + B*(Y-X), C*(2*Y)))
    else:
        print(min(C*(2*Y) + A*(X-Y), C*(2*X)))

# 自分の解答(OK)
# cost = [0]*3
# # ピザABを含む場合
# X1, Y1 = X, Y
# common = max(X, Y) - abs(X - Y)
# X1 -= common
# Y1 -= common
#
# cost[0] += C * (2 * common)
# cost[0] += A * X1
# cost[0] += B * Y1
#
# # ピザABを含まない場合
# cost[1] += A * X
# cost[1] += B * Y
#
# # ピザABのみの場合
# if X >= Y:
#     cost[2] += C * (2 * X)
# else:
#     cost[2] += C * (2 * Y)
#
# ans = min(cost)
# print(ans)
