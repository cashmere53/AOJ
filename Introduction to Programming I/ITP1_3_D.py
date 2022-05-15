a, b, c = map(int, input().split(" "))
count: int = 0
for i in range(a, b + 1):
    count += 1 if (c % i) == 0 else 0
print(count)
