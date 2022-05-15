w, h, x, y, r = map(int, input().split(" "))
area = {(x, y) for x in range(r, w - r + 1) for y in range(r, h - r + 1)}
print("Yes" if (x, y) in area else "No")
