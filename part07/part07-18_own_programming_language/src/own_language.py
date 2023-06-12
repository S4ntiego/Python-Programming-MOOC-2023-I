# Write your solution here
import string


def determine_value(input: str, variables: dict):
    if input in string.ascii_uppercase:
        return variables[input]
    else:
        return int(input)


def run(program: list):
    val_to_print = []
    variables = {}
    for letter in string.ascii_uppercase:
        variables[letter] = 0

    locations = []
    for index, cmd in enumerate(program):
        if ":" in cmd:
            location = cmd[:-1]
            locations.append((location, index))

    i = 0
    while i < len(program):
        ins = program[i]
        commands = ins.split(" ")
        action = commands[0]
        if action == "MOV":
            val = determine_value(commands[2], variables)
            variables[commands[1]] = val
        elif action == "PRINT":
            val = determine_value(commands[1], variables)
            val_to_print.append(val)
        elif action == "ADD":
            val = determine_value(commands[2], variables)
            variables[commands[1]] += val
        elif action == "SUB":
            val = determine_value(commands[2], variables)
            variables[commands[1]] -= val
        elif action == "MUL":
            val = determine_value(commands[2], variables)
            variables[commands[1]] *= val
        elif action == "JUMP":
            jump_to = commands[1]
            for loc in locations:
                if loc[0] == jump_to:
                    i = loc[1]
        elif action == "IF":
            variable = str(determine_value(commands[1], variables))
            condition = commands[2]
            value = str(determine_value(commands[3], variables))
            result = eval(variable + condition + value)
            if result == True:
                jump_to = commands[5]
                for loc in locations:
                    if loc[0] == jump_to:
                        i = loc[1]
        elif action == "END":
            return val_to_print

        i += 1
    return val_to_print


if __name__ == "__main__":
    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)
