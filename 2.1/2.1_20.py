n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
for x in range(n):
    for y in range(n):
        if k1 * x + k2 * y == n * m and x + y == n:
            print(x, y)
