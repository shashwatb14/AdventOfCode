lights = {}

# populate dictionary
for i in range(1000):
    for j in range(1000):
        lights[f"{i}, {j}"] = "X"


def change_status(start_coords, end_coords, status):
    for i in range(start_coords[0], end_coords[0] + 1):
        for j in range(start_coords[1], end_coords[1] + 1):
            lights[f"{i}, {j}"] = status


def toggle(start_coords, end_coords):
    for i in range(start_coords[0], end_coords[0] + 1):
        for j in range(start_coords[1], end_coords[1] + 1):
            if lights[f"{i}, {j}"] == "O": lights[f"{i}, {j}"] = "X"
            else: lights[f"{i}, {j}"] = "O"

with open("./2015/day6/data.txt", "r") as f:
    for line in f:
        start_coords = []
        end_coords = []

        start_coords.append(int(line.split(",")[0].split()[-1]))
        start_coords.append(int(line.split(",")[1].split()[0]))
        end_coords.append(int(line.split(",")[1].split()[-1]))
        end_coords.append(int(line.split(",")[-1].split("\n")[0]))

        if "turn on" in line: change_status(start_coords, end_coords, "O")
        elif "turn off" in line: change_status(start_coords, end_coords, "X")
        else: toggle(start_coords, end_coords)

on = 0

for value in lights.values():
    if value == "O": on += 1

print(on)

# answer: 377891