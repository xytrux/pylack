memory = [0] * 100
counter_ptr = 0
comment = 0

with open("main.bl", "r") as file:
    for c in file.read():
        if c == ';':
            comment = not comment
        elif c == '[':
            memory[counter_ptr] += 1
        elif c == ']':
            memory[counter_ptr] -= 1
        elif c == '*':
            memory[counter_ptr] *= 2
        elif c == ',':
            memory[counter_ptr] *= 3
        elif c == '(':
            counter_ptr += 1
        elif c == ')':
            counter_ptr -= 1
        elif c == '.':
            print(chr(memory[counter_ptr]), end='')
        elif c == '%':
            memory = [0] * 100
        elif c == '#':
            memory[counter_ptr] = 0
        elif c == '@':
            print(memory[counter_ptr])
        elif c == '/':
            print()
        elif c == '&':
            print(" ", end='')
