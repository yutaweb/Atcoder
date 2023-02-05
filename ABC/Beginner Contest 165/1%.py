X = int(input())

n = 100
count = 0
while n < X:
    count += 1
    n += int(n * 1.01)

print(count)
