num = int(input())

out = ""
format = lambda x: f" {i}"

def digit(n):
    while n != 0:
        yield n
        n //= 10

for i in range(1, num + 1):
    if i % 3 == 0:
        out += format(i)
        continue
    for d in digit(i):
        if d % 10 == 3:
            out += format(i)
            break

print("".join(out))
