class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def tree(nums, depth):
    children = [Node(num) for num in nums]
    while depth > 0:
        parents = []
        for i in range(0, 2**(depth)-1, 2):
            parents.append(Node())
            parents[-1].children.append(children[i])
            parents[-1].children.append(children[i+1])
        children = parents
        depth -= 1
    return children[0]

def minimax(node, depth, alpha, beta, maximizing):
    if depth == 0:
        return node.value

    if maximizing:
        maxEval = -float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            if maxEval >= beta:
                break
            alpha = max(alpha, maxEval)
        return maxEval
    else:
        minEval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            if minEval <= alpha:
                break
            beta = min(beta, minEval)
        return minEval

def pacman_game(c):
    outcomes = [3, 6, 2, 3, 7, 1, 2, 0]

    depth = 2
    root = tree(outcomes, depth)

    minimax_value_without_magic = minimax(root, depth, -float('inf'), float('inf'), True)

    left_subtree = root.children[0]
    left_with_magic = minimax(left_subtree, depth - 1, -float('inf'), float('inf'), True) - c

    right_subtree = root.children[1]
    right_with_magic = minimax(right_subtree, depth - 1, -float('inf'), float('inf'), True) - c

    best_with_magic = max(left_with_magic, right_with_magic)

    if best_with_magic > minimax_value_without_magic:
        print(f"The new minimax value is {best_with_magic}. Pacman uses dark magic")
    else:
        print(f"The minimax value is {minimax_value_without_magic}. Pacman does not use dark magic")


pacman_game(2)
pacman_game(5)
