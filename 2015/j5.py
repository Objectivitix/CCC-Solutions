import functools

@functools.cache
def find_partitions_n(prev, n, k):
    if k == 1:
        return 1

    partitions_n = 0

    for choice in range(prev or 1, n):
        if choice * (k - 1) > n - choice:
            break

        partitions_n += find_partitions_n(choice, n - choice, k - 1)

    return partitions_n

n = int(input())
k = int(input())

print(find_partitions_n(None, n, k))
