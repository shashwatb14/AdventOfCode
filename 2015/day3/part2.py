c = 0
locs = []


def calculate(i, coord):
    global c, locs

    if i == "^": coord[1] += 1
    elif i == ">": coord[0] += 1
    elif i == "v": coord[1] -= 1
    else: coord[0] -= 1
    
    if coord not in locs: 
        locs.append(coord.copy()) # create a copy to avoid referencing to the same list
        c += 1

with open("./2015/day3/data.txt", "r") as f:
    robo_coord = [0, 0]
    santa_coord = [0, 0]

    for i, n in enumerate(f.read()):
        if i % 2 == 0: calculate(n, santa_coord)
        else: calculate(n, robo_coord)

    print(c)

# answer: 2631