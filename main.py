import sys
import os

memory = [0] * 100
counter_ptr = memory
comment = 0

if len(sys.argv) != 2:
    print("Usage: bl <filename>.bl")
    sys.exit(1)

filename = sys.argv[1]
file_extension = os.path.splitext(filename)[1]

if file_extension != '.bl':
    print("Error: File must have a .bl extension")
    sys.exit(1)

try:
    with open(filename, "r") as file:
        for c in file.read():
            if c == ';':
                comment = not comment
            elif c == '[':
                counter_ptr[0] += 1
            elif c == ']':
                counter_ptr[0] -= 1
            elif c == '*':
                counter_ptr[0] *= 2
            elif c == ',':
                counter_ptr[0] *= 3
            elif c == '(':
                counter_ptr = counter_ptr[1:]
            elif c == ')':
                counter_ptr = [0] + counter_ptr
            elif c == '.':
                print(chr(counter_ptr[0]), end='')
            elif c == '%':
                memory = [0] * 100
            elif c == '#':
                counter_ptr[0] = 0
            elif c == '@':
                print(counter_ptr[0])
            elif c == '/':
                print()
            elif c == '&':
                print(" ", end='')
except FileNotFoundError:
    print(f"Error: Cannot open file {filename}")
