class Node:
    def __init__(self, id_value):
        self.id_value = id_value # node ID
        self.left = None  # left child
        self.right = None # right child
        self.time = None  # length of time since parent node

def insert(root, id_value): # insert node
    if root is None:
        return Node(id_value)
    else:
        if id_value < root.id_value:
            root.left = insert(root.left, id_value)
        else:
            root.right = insert(root.right, id_value)
        return root
    
def generate(root, generation): # generate root node
    if root is None:
        x = 2**(generation-1)
        root = insert(root, x)
        return root
    else:
        print("tree is not empty")

def left_from_node(root, node, generation):
    # from node 2 on generation 5 (6144), add a node to the left (5120)
    if node <= 2**(generation-1):
        x = 2**(16-generation) 
        while node > 1:
            x = x + 2**(17-generation) # parent node value 
            node -= 1
        y = x - 2**(15-generation)
        # insert node
        root = insert(root, y)
    else:
        print("node value is too high")

def right_from_node(root, node, generation):
    # from node 7 on generation 8 (3328), add a node to the right (3456)
    if node <= 2**(generation-1):
        x = 2**(16-generation)
        while node > 1:
            x = x + 2**(17-generation)
            node -= 1
        y = x + 2**(15-generation)
        #insert node
        root = insert(root, y)
    else:
        print("node value is too high")

def preorder_traversal(lst,root):
    if root:
        lst.append(root.id_value)
        preorder_traversal(lst,root.left)
        preorder_traversal(lst,root.right)
        
def traverse_node_to_root(root, target):
    if root is None:
        return []
    
    path = []
    current = root
    
    while current:
        path.append(current.id_value)
        
        if current.id_value == target:
            return path[::-1]
        elif target < current.id_value:
            current = current.left
        else:
            current = current.right
    return(len(path))

def traverse_root_to_node(root, target):
    if root is None:
        return []
    
    path = []
    current = root
    
    while current:
        path.append(current.id_value)
        
        if current.id_value == target:
            return path[::1]
        elif target < current.id_value:
            current = current.left
        else:
            current = current.right
    return(len(path))

def input_node(root, file):

    with open(file, 'r') as f:
    # keep going until we exhaust the file
        while True:
        # read the next four lines of the file
            side = f.readline().strip()
            try:
                node = int(f.readline().strip())
                gen = int(f.readline().strip())
            except ValueError:
                break
            
            if side == "l":
                left_from_node(root, node, gen)
            elif side == "r":
                right_from_node(root, node, gen)
            else:
                break

def display(root):
    chart = []
    preorder_traversal(chart,root)
    display_chart = chart.copy()
    i = 0
    while i < len(chart):
        x = len(traverse_node_to_root(root, chart[i]))
        if x > 1:
            display_chart[i] = "  └──" + str(display_chart[i])
        if x > 2:
            while x > 2:
                display_chart[i] = "     " + str(display_chart[i])
                x -= 1
        i += 1

    k = len(display_chart)-1
    while k > 0:
        a = str(display_chart[k]).find('└')
        if str(display_chart[k])[a] == '└' and str(display_chart[k-1])[a] == ' ':
            display_chart[k-1] = str(display_chart[k-1])[:a] + '│' + str(display_chart[k-1])[a + 1:]
        else:
            pass
        
        b = str(display_chart[k]).find('│')
        if str(display_chart[k])[b] == '│' and str(display_chart[k-1])[b] == ' ':
            display_chart[k-1] = str(display_chart[k-1])[:b] + '│' + str(display_chart[k-1])[b + 1:]
        else:
            pass

        c = str(display_chart[k]).find('└')
        if str(display_chart[k])[c] == '└' and str(display_chart[k-1])[c] == '└':
            display_chart[k-1] = str(display_chart[k-1])[:c] + '├' + str(display_chart[k-1])[c + 1:]
        else:
            pass

        d = str(display_chart[k-1]).find('└')
        if d > len(str(display_chart[k])):
            pass
        elif str(display_chart[k-1])[d] == '└' and str(display_chart[k])[d] == '│':
            display_chart[k-1] = str(display_chart[k-1])[:d] + '├' + str(display_chart[k-1])[d + 1:]
        else:
            pass
        k -= 1

    z = 0
    while z < len(display_chart):
        print(display_chart[z])
        z += 1
    display_chart.clear()
    chart.clear()
