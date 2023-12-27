def get_contiguous_subarrays(arr, arr_length, subarr_length):
    for i in range(arr_length - subarr_length + 1):
        yield arr[i:i + subarr_length]

word = input()
w_length = len(word)

rows_n = int(input())
columns_n = int(input())

mat = [
    input().split()
    for _ in range(rows_n)
]
mat_prime = list(zip(*mat))

occurences_n = 0

for row in mat:
    for subarr in get_contiguous_subarrays(row, columns_n, w_length):
        tentative = "".join(subarr)
        if tentative == word or tentative[::-1] == word:
            occurences_n += 1

for column in mat_prime:
    for subarr in get_contiguous_subarrays(column, rows_n, w_length):
        tentative = "".join(subarr)
        if tentative == word or tentative[::-1] == word:
            occurences_n += 1

print(occurences_n)
