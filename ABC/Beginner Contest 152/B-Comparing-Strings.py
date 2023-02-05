a, b = map(int, input().split())

a_temp = str(a) * b
b_temp = str(b) * a

if a_temp > b_temp:
    print(b_temp)
else:
    print(a_temp)

