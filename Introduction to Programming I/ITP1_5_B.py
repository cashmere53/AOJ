while True:
    h, w = map(int, input().split(" "))
    if h == w == 0:
        break

    print(
        "\n".join(
            [
                "#" * w,
                *([("#" + ("." * (w - 2)) + "#")] * (h - 2)),
                "#" * w,
            ]
        ),
        end="\n\n"
    )
