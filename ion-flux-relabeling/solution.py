def traverse(height, node):
    nodes = 2 ** height - 1
    root_node = nodes

    if root_node == node:
        return -1

    # initialize parent node with initial root
    parent_node = root_node
    # next level after the root node
    level = height - 1

    while level > 0:

        right_node = parent_node - 1
        left_node = right_node - (2 ** level - 1)
        print(
            f"level: {level} \n {left_node} <- {parent_node} -> {right_node}"
        )

        # check if they're leafs of parent node
        if (node == right_node) or (node == left_node):
            return parent_node

        # if current node greater than left node the parent is the right node
        if node > left_node:
            parent_node = right_node
        else:
            parent_node = left_node

        # parent not found in current level recursively check next lower level
        level -= 1


def solution(h, q):
    soln = []

    for node in q:
        soln.append(traverse(h, node))

    return soln
