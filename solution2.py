def has_subset_with_sum_k(A, S, i):
    if S == 0:
        return True
    if i >= len(A):
        return False
    if A[i] == S:
        return True

    return has_subset_with_sum_k(A, S - A[i], i + 1) or has_subset_with_sum_k(A, S, i + 1)


def solution():
    array = list(map(int, input().split()))
    s = int(input().strip())
    c = has_subset_with_sum_k(array, s, 0)
    print(c)


if __name__ == '__main__':
    solution()
