values = {}
instructions = []
cmds = {
    "AND": "&",
    "OR": "|",
    "LSHIFT": "<<",
    "RSHIFT": ">>",
    "NOT": "~"
}

with open("./2015/day7/data.txt", "r") as f:
    for line in f:
        if "1674 -> b" not in line:
            instructions.append(line)
            values[line.split()[-1]] = ""
        else: values['b'] = 46065

while values['a'] == "":
    for line in instructions:
        try:
            expression = line.split(" ->")[0]
            if "NOT" in expression:
                result = f"~ {values[line.split(' ->')[0].split()[1]]}"
                result = eval(result)

            elif len(expression.split()) == 3:
                if "RSHIFT" in expression or "LSHIFT" in expression:
                    result = f"{values[expression.split()[0]]} {cmds[expression.split()[1]]} {expression.split()[-1]}"
                
                else:
                    if f"{expression.split()[0]}".isnumeric():
                        result = f"{expression.split()[0]} {cmds[expression.split()[1]]} {values[expression.split()[-1]]}"
                    else:
                        result = f"{values[expression.split()[0]]} {cmds[expression.split()[1]]} {values[expression.split()[-1]]}"

                result = eval(result)
            
            elif len(expression.split()) == 1:
                if expression.isnumeric(): result = eval(expression)
                else: result = eval(f"{values[expression]}")

            values[line.split()[-1]] = result
            instructions.remove(line)
        except: pass

print(values['a'])

# answer: 14134
