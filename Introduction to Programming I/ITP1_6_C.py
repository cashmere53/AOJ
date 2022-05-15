condo = []
for _ in range(4):
    arr1 = []
    for _ in range(3):
        arr1.append([0 for _ in range(10)])
    condo.append(arr1)

n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split(" "))
    condo[b - 1][f - 1][r - 1] += v

str1 = []
for house in condo:
    str2 = []
    for floor in house:
        floor_map = map(lambda x: f" {x}", floor)
        str2.append("".join(floor_map) + "\n")
    str1.append("".join(str2))
print(("#" * 20 + "\n").join(str1), end="")
