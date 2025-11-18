import random

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def tree(depth):
    half = int((2**depth)/2)
    children = [Node(1)]*(half) + [Node(-1)]*(half)
    random.shuffle(children)
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

def simulate_game():
    start_player = int(input())

    scorpion_won = 0
    subzero_won = 0
    rounds = 0
    round_winners = []
    current_player = start_player
    while rounds <= 3:
        maximizing = True if current_player == 1 else False
        game_tree = tree(5)
        result = minimax(game_tree, 5, -float('inf'), float('inf'), maximizing)
        if result == -1:
            scorpion_won += 1
            round_winners.append("Scorpion")
        elif result == 1:
            subzero_won += 1
            round_winners.append("Sub-Zero")
        rounds += 1
        if rounds == 1:
            current_player = 0 if current_player == 1 else 1
        if scorpion_won == 2 or subzero_won == 2:
            break

    print("="*40)
    if scorpion_won > subzero_won:
        print("Game Winner: Scorpion")
    else:
        print("Game Winner: Sub-Zero")
    print(f"Total Rounds Played: {rounds}")
    for i in range(rounds):
        print(f"Winner of Round {i+1}: {round_winners[i]}")

simulate_game()