data = [input() for i in range(3)]

x = []
y = []
for d in data:
    x.append(d.split()[0])
    y.append(d.split()[1])

for data in x:
    if x.count(data) == 1:
        ans_x = data
        break

for data in y:
    if y.count(data) == 1:
        ans_y = data
        break

print(f'{ans_x} {ans_y}')
