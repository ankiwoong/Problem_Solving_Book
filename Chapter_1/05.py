def ox(n):
    for i in range(1, n + 1):
        print("0" * (n - i) + "X" * i)


ox(6)
