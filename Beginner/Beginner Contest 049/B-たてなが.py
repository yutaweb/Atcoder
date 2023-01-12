H, W = map(int, input().split())
C = [input() for _ in range(H)]

# 2倍縦長にした画像を出力する
for i in range(len(C)):
    print(C[i])
    print(C[i])
