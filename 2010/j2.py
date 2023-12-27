def good(forward, backward, steps):
    compl, remain = divmod(steps, forward + backward)
    last = remain if remain <= forward else forward - (remain - forward)
    return compl * (forward - backward) + last

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

one = good(a, b, s)
two = good(c, d, s)

print(
    "Nikky" if one > two else
    "Tied" if one == two else
    "Byron"
)
