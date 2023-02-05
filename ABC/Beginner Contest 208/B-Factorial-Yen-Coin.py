import math

P = int(input())


def detect_factorial(num):
    i = 1
    while True:
        temp = math.factorial(i)
        if i > 10:
            temp = math.factorial(10)
            break
        if temp > num:
            temp = math.factorial(i - 1)
            break
        if temp == num:
            break
        i = i + 1

    return temp


counter = 0
while P != 0:
    P = P - detect_factorial(P)
    counter = counter + 1

print(counter)
