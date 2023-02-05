S = input()
T = input()


def check(s, t):
    if s == t:
        return True

    for i in range(len(s)):
        temp = ""
        temp += s[len(s)-i-1:] + s[:len(s)-i-1]
        if temp == t:
            return True
    return False


print("Yes" if check(S, T) else "No")
