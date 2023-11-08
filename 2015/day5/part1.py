with open("./2015/day5/data.txt", "r") as f:
    c = 0

    unacceptable = ["ab", "cd", "pq", "xy"]
    vowels = ["a", "e", "i", "o", "u"]

    for line in f:

        can = True
        double = False
        v = 0

        for i in range(len(line) - 1):

            if line[i:i + 2] in unacceptable:
                can = False
                break

            if line[i] == line[i + 1]: double = True
            if line[i] in vowels: v += 1

        if double and v > 2 and can: c += 1
    
    print(c)

# answer: 236