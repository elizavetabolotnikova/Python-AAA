def fib(n, i, j):  # не меняйте название функции (агрументы можно менять)
    cnt = i + j
    if n == 0:
        return 1
    elif n == 1:
        return cnt
    else:
        return fib(n - 1, j, cnt)


def solution():
    n = int(input().strip())
    c = fib(n, 0, 1)
    print(c)


if __name__ == '__main__':
    solution()
