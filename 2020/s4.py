# Pretty cool problem. O(N) solution, gets full points.

from itertools import accumulate


def cum_count(target):
    return lambda prev, char: prev + (char == target)


def wrapped_count(start, end, target, cums, n):
    intervals = (
        [(start % n, end % n)] if start >= n
        else [(start, end)] if end < n
        else [(start, n), (0, end % n)]
    )

    return sum(
        cums[target][w_end] - cums[target][w_start]
        for w_start, w_end in intervals
    )


def min_swaps(a_start, x, cums, n):
    """
    Minimum swaps needed if the contiguous group containing A
    starts at `a_start` and is followed by the contiguous group
    containing `x`.
    """
    other, = set("ABC") - {"A", x}

    a_count = cums["A"][-1]
    x_count = cums[x][-1]

    a_end = a_start + a_count
    x_end = a_end + x_count

    x_in_a = wrapped_count(a_start, a_end, x, cums, n)
    a_in_x = wrapped_count(a_end, x_end, "A", cums, n)

    savings = min(x_in_a, a_in_x)

    other_in_a = wrapped_count(a_start, a_end, other, cums, n)
    other_in_x = wrapped_count(a_end, x_end, other, cums, n)

    return x_in_a + other_in_a + a_in_x + other_in_x - savings


SEATS = input()
N = len(SEATS)

CUMS = {
    c: list(accumulate([0, *SEATS], cum_count(c)))
    for c in "ABC"
}

print(min(
    min_swaps(a_start, following, CUMS, N)
    for a_start in range(N)
    for following in "BC"
))
