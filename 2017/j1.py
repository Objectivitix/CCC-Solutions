POSITIVE_COORDS_TO_QUADRANTS = {
    (True, True): 1,
    (False, True): 2,
    (False, False): 3,
    (True, False): 4,
}

x = int(input())
y = int(input())

print(POSITIVE_COORDS_TO_QUADRANTS[
    x > 0,
    y > 0,
])
