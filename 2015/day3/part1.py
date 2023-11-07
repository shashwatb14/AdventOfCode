with open("./2015/day3/data.txt", "r") as f:
    locs = []
    coord = [0, 0]
    c = 0

    for i in f.read():
        if i == "^": coord[1] += 1
        elif i == ">": coord[0] += 1
        elif i == "v": coord[1] -= 1
        else: coord[0] -= 1
        
        if coord not in locs: 
            locs.append(coord.copy()) # create a copy to avoid referencing to the same list
            c += 1

    print(c)

# answer: 2572
