n1, n2 = map(int, input().split(" "))
op = lambda a, b: ">" if (a > b) else ("==" if (a == b) else "<")
print(f"a {op(n1, n2)} b")