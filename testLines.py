t = int(input())
for i in range(1, t + 1):
    n = int(input())
    a = int("".join("1" if d == "4" else "0" for d in str(n)), 10)
    print(a)
    b = n - a
    print("Case #{}: {} {}".format(i, a, b))