def main():
    # 入力値を取得
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # up or down
    base = A[0]
    for i in range(1, N):
        diff = base - A[i]
        if diff == 0:
            ans = "stay"
        elif diff < 0:
            ans = "up " + str(abs(diff))
        else:
            ans = "down " + str(abs(diff))

        base = A[i]

        print(ans)


if __name__ == "__main__":
    main()
