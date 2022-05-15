from operator import add, floordiv, mul, sub


ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv,
}

while True:
    a, op, b = input().split(" ")
    a, b = map(int, [a, b])
    if op == "?":
        break
    print(ops[op](a, b))
