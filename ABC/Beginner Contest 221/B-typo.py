S = list(input())
T = list(input())


def check(s, t):
    if s == t:
        return True

    for i in range(len(s) - 1):
        s_copy = s.copy()
        temp = s_copy[i]
        s_copy[i] = s_copy[i+1]
        s_copy[i+1] = temp
        if s_copy == t:
            return True

    return False


print("Yes" if check(S, T) else "No")
