n = int(input())
d = {f"{m} {v}": False for m in ["S", "H", "C", "D"] for v in range(1, 14)}

for _ in range(n):
    card = input()
    d[card] = True

for k, v in d.items():
    if not v:
        print(k)
