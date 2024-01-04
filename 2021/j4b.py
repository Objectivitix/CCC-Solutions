BOOKS = input()

L = BOOKS.count("L")
M = BOOKS.count("M")

L_SECTION = BOOKS[:L]
M_SECTION = BOOKS[L:L + M]

m_in_l = L_SECTION.count("M")
l_in_m = M_SECTION.count("L")

print(
    m_in_l
    + L_SECTION.count("S")
    + l_in_m
    + M_SECTION.count("S")
    - min(m_in_l, l_in_m)  # swaps that can be saved
)
