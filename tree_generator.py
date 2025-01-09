from binary_tree import *
# Tree text file generator
    
def write_file():
    filename = input('name new file:')
    filename = filename + ".txt"

    text = []
    # add lines to text[]
    while True:
        side = input('l/r:')

        if side == 'l':
            node = int(input('node:'))
            gen = int(input('generation:'))
            text.append(side)
            text.append(str(node))
            text.append(str(gen))
        elif side == 'r':
            node = int(input('node:'))
            gen = int(input('generation:'))
            text.append(side)
            text.append(str(node))
            text.append(str(gen))
        else:
            break

    with open(filename, "w") as f:
        for line in text:
            f.write(line + "\n")  # Add newline character to write each line on a new line
