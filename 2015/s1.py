k = int(input())

stack = []

for _ in range(k):
    num = int(input())

    if num == 0:
        stack.pop()
        continue

    stack.append(num)

print(sum(stack))
