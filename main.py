from binary_tree import *

if __name__ == "__main__":

    while True:
        # main menu to select between creating / opening a tree
        root = None
        root = generate(root,16)
        file = input('open: ')
        input_node(root, file) # input from file
        display(root)
        close = input('open new/close [o/any]:')
        if close == 'o':
            pass
        else:
            break
