from collections import defaultdict


N = int(input())

# 配列から取り除くべき要素の数を数える
A = map(int, input().split())
Sequence = defaultdict(int)
for a in A:
    Sequence[a] += 1

cnt = 0
for item in Sequence.items():
    if item[0] > item[1]:
        cnt += item[1]
    elif item[0] < item[1]:
        cnt += item[1] - item[0]

print(cnt)
