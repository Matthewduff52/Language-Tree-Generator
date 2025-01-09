# Tree text file generator
def write_file():
    filename = input('name new file:') # take file name input
    filename = filename + ".txt"

    text = [] # empty array for loading text data

    while True:
        side = input('l/r:') # is new node on the left or right of parent

        if side == 'l':
            node = int(input('node:')) # parent node how many nodes from the left (on a complete tree)
            gen = int(input('generation:')) # child node distance from root
            text.append(side) # load text data into array
            text.append(str(node))
            text.append(str(gen))
        elif side == 'r':
            node = int(input('node:'))
            gen = int(input('generation:'))
            text.append(side)
            text.append(str(node))
            text.append(str(gen))
        else:
            break # end file construction

    with open(filename, "w") as f: # create or edit existing file
        for line in text:
            f.write(line + "\n")  # Add newline character for file formatting
