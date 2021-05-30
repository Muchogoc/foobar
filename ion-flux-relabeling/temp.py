class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def create_perfect_tree(depth):
    # number of nodes
    nodes = 2**(depth + 1) - 1
    # create binary tree
    root = insert (None,nodes)
    while nodes > 1:
        nodes =- 1
        insert(root,nodes)
    
    return root

def insert(root,value):
    if root is None:
        root = Node(value)
        return root
    
    if value < root.data:
        root.left = insert(root,value)
    else:
        root.right = insert(root.value)
        
    return root
    
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

if __name__ == "__main__":
    tree = create_perfect_tree(2)
    postorder(tree)
