H, W = map(int, input().split())

counter = 0
for _ in range(H):
    s = input()
    counter += s.count('#')

print(counter)
