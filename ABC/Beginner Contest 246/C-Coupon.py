N, K, X = map(int, input().split())
data = list(map(int, input().split()))
range_num = K

for _ in range(range_num):
    data = sorted(data, reverse=True)
    for i, v in enumerate(data):
        calc = v - X
        if calc >= 0 and K > 0:
            data[i] = calc
            K -= 1
        else:
            break

data = sorted(data, reverse=True)
for i, v in enumerate(data):
    calc = max(v - X, 0)
    if calc >= 0 and K > 0:
        data[i] = calc
        K -= 1
    else:
        break

print(sum(data))


"""
1. 大きい順にソートを掛ける
2. 非負になるまで引き続ける
3. 大きい順にソートを掛ける
4. 余っているクーポン分を引く
"""