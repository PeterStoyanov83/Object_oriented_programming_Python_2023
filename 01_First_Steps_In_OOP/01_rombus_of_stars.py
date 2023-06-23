def print_stars(n, count):
    print(" " * (num - count), end="")
    print(*["*"] * count)


num = int(input())

for count in range(1, num + 1):
    print_stars(num, count)

for count in range(num - 1, 0, -1, ):
    print_stars(num, count)
