start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
t = int(input())

dist = abs(start[0] - end[0]) + abs(start[1] - end[1])

print("Y" if t >= dist and t & 1 == dist & 1 else "N")
