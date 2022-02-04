S = input()
if S == S[::-1]:
    print("Yes")
    exit()

flag = True
length = len(S) - 1
while flag:
    s = S[length]
    if s == "a":
        S = "a" + S
        length = len(S) - 1
        if S == S[::-1]:
            print("Yes")
            flag = False
    else:
        print("No")
        flag = False
    length -= 1