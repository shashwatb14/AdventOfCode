with open("./2015/day1/data.txt", "r") as f:
    x = 0
    for i in f.read():
        if i == "(": x += 1
        else: x -= 1

    print(x)

# answer: 74