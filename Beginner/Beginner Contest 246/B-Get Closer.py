import math

data = list(map(int, input().split()))

x = data[0]
y = data[1]
z = math.sqrt(x**2 + y**2)

x_move = x / z
y_move = y / z
print(f'{x_move} {y_move}')