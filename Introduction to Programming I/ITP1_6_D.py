matrix_a = []
matrix_b = []

n, m = map(int, input().split(" "))
for _ in range(n):
    matrix_a.append(list(map(int, input().split(" "))))
for _ in range(m):
    matrix_b.append(int(input()))

matrix_c = []
for ma in matrix_a:
    sum = 0
    for a, b in zip(ma, matrix_b):
        sum += a * b
    matrix_c.append(sum)
for c in matrix_c:
    print(c)
