N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
count = 0
i = 0
ans = 0

# コメント
while True:
    # 配列の長さの制御を入れる。
    print(f'Before A : {A}')
    if len(A) < K:
        break
    if A[i] >= 1:
        A[i] = A[i] - 1
        if A[i] == 0:
            A.pop(i)
            i = 0  # popしたので、0に戻す必要がある
            print(f'pop i : {i}')
        else:
            if i == K - 1:
                i = 0
            else:
                i += 1
            print(f'i : {i}')
        count += 1
        print(f'After A : {A}')
        print(f'count : {count}')

    if count == K:
        ans += 1
        count = 0
        print(f'ans : {ans}')
# print(f'N : {N} K : {K}')
# print(f'A : {A}')
print(A, count, ans)

# 手順
# Aを昇順に並べ替える
# While文のループに入る
# 配列の長さがKよりも小さければbreak
# A[i]が1以上であるか判定する
# 1以上であれば、K個分の要素に対して1を減じる
# 上記を要素の値が0になるまで繰り返す。
# 0になったらpopで取り除く
#

