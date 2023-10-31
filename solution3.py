def move(n, b, c):
    s = []
    if n == 1:
        s.append(n)
        s.append(b)
        s.append(c)
        print(*s)
        return
    else:
        move(n - 1, b, 6 - b - c)
        print(n, b, c)
        move(n - 1, 6 - b - c, c)

def solution():
    move(int(input()), 1, 3)

if __name__ == '__main__':
    solution()

