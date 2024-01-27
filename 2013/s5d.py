# http://mmhs.ca/ccc/2013/ccc2013s5fast.txt
# what the heck guys

n = int(input())
cost = 0

while n > 1:
    for i in range(2, int(n) + 1):
        factor = n / i

        if not factor.is_integer():
            continue

        n -= factor
        cost += n / factor
        break

print(int(cost))
