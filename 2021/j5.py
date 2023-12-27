m = int(input())
n = int(input())

k = int(input())
brushes = (
    input().split()
    for _ in range(k)
)

rows_active_n = 0
columns_active_n = 0

rows = {}
columns = {}

gold = 0

for direction, pos in brushes:
    if direction == "R":
        if rows.get(pos, False):
            rows_active_n -= 1
            rows[pos] = False
            gold -= n - columns_active_n - columns_active_n
        else:
            rows_active_n += 1
            rows[pos] = True
            gold += n - columns_active_n - columns_active_n

    if direction == "C":
        if columns.get(pos, False):
            columns_active_n -= 1
            columns[pos] = False
            gold -= m - rows_active_n - rows_active_n
        else:
            columns_active_n += 1
            columns[pos] = True
            gold += m - rows_active_n - rows_active_n

print(gold)
