A, B = map(int, input().split())

count = 0
for v in range(A, B + 1):
    to_str = str(v)
    if to_str[:2] == to_str[-2:]:
        count = count + 1

print(count)
