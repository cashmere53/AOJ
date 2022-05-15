def c(w, h):
    return "#" if (w + h) % 2 == 0 else "."

while True:
    h, w = map(int, input().split(" "))
    if h == w == 0:
        break

    string = [[c(i, j) for i in range(w)] for j in range(h)]
    string = ["".join(item) + "\n" for item in string]
    string = "".join(string)
    print(string)
