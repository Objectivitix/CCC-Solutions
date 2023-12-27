SCOVILLES = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000,
}

n = int(input())

s = 0

for _ in range(n):
    pepper = input()
    s += SCOVILLES[pepper]

print(s)
