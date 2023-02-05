import numpy as np

x, y, degree = map(int, input().split())


def get_rotation_matrix(rad):
    """
    指定したradの回転行列を返す
    """
    rotation = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
    return rotation


base_point = np.array([x, y])
radian = degree * np.pi / 180
rot = get_rotation_matrix(radian)
rotated = np.dot(rot, base_point)
print(*rotated)
