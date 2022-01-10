"""
AN≦1000W≦BNであれば、Yesそれ以外は、No
"""
import math


A, B, W = map(int, input().split())

lower = int(math.floor(1000*W/A))
upper = int(math.ceil(1000*W/B))

if lower > upper:
    print("UNSATISFIABLE")
else:
    print(f"{lower} {upper}")