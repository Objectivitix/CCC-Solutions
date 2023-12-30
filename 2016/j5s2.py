mode = input()
_ = input()
a_arr = sorted(map(int, input().split()))
b_arr = sorted(map(int, input().split()))

if mode == "1":
    print(sum(max(a, b) for a, b in zip(a_arr, b_arr)))
elif mode == "2":
    print(sum(max(a, b) for a, b in zip(a_arr, b_arr[::-1])))
