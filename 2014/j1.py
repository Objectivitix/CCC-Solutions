from itertools import combinations

angles = [
    int(input())
    for _ in range(3)
]

if sum(angles) != 180:
    print("Error")

elif all(angle == 60 for angle in angles):
    print("Equilateral")

elif any(angle_a == angle_b for angle_a, angle_b in combinations(angles, 2)):
    print("Isosceles")

else:
    print("Scalene")
