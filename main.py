from binary_tree import * #read_file()
from tree_generator import * #write_file()

if __name__ == "__main__":
    while True:
        x = input('menu [new/open]:') # main menu
        if x == 'new':
            write_file() # write a new tree file
        elif x == 'open':
            read_file() # read an existing tree file
        else:
            break # end program
