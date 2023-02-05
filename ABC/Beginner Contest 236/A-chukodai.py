def main(S, a, b):
    Before = S[:a]
    Middle = S[a+1:b]
    After = S[b+1:]
    ans = Before + S[b] + Middle + S[a] + After
    print(ans)


if __name__ == "__main__":
    S = input()
    a, b = map(int, input().split())
    main(S, a - 1, b - 1)