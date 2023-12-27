_ = input()

a = input()
b = input()

a_int = int(a.replace("C", "1").replace(".", "0"), base=2)
b_int = int(b.replace("C", "1").replace(".", "0"), base=2)

both = a_int & b_int

print(bin(both).count("1"))
