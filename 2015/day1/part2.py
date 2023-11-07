with open("./2015/day1/data.txt", "r") as f:
    x = 0
    c = 1

    for i in f.read():
        if i == "(": x += 1
        else: x -= 1

        if x == -1:
            print(c)
            break

        c += 1

# answer: 1795