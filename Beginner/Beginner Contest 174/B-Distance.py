import numpy as np


N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]


def calc_distance(points):
    x = points[0]
    y = points[1]
    distance = np.sqrt(x**2 + y**2)
    if distance <= D:
        return 1
    return 0


counter = 0
for i in range(N):
    counter += calc_distance(XY[i])

print(counter)
