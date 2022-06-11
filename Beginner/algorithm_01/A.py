def main():
    s = input()
    if is_int(s[0]) and is_int(s[1]) and is_int(s[2]):
        ans = int(s) * 2
    else:
        ans = "error"

    print(ans)


def is_int(data):
    return data in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


if __name__ == "__main__":
    main()
