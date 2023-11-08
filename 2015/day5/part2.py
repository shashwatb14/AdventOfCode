with open("./2015/day5/data.txt", "r") as f:
    c = 0

    for line in f:
        repeat = False
        twice = False
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]: repeat = True

            for j in range(len(line) - 2):
                if line[i:i + 2] == line[j:j + 2] and abs(i - j) > 1: twice = True

        if repeat and twice: c += 1
    
    print(c)

# answer: 51