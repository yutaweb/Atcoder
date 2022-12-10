S = input()
T = input()


def check(s, t):
    if s < t:
        return True

    if ''.join(sorted(s)) < ''.join(sorted(t, reverse=True)):
        return True

    return False


print("Yes" if check(S, T) else "No")

