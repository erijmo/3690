def alpha_beta(node, alpha, beta, maximizing_player):
    if not game_tree[node]["children"]:
        return game_tree[node]["value"]

    if maximizing_player:
        best_value = float('-inf')
        for child in game_tree[node]["children"]:
            child_value = alpha_beta(child, alpha, beta, False)
            best_value = max(best_value, child_value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float('inf')
        for child in game_tree[node]["children"]:
            child_value = alpha_beta(child, alpha, beta, True)
            best_value = min(best_value, child_value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value


game_tree = {
    0: {"value": 5, "children": [1, 2]},
    1: {"value": 5, "children": [3, 4]},
    2: {"value": 5, "children": [5, 6]},
    3: {"value": 5, "children": []},
    4: {"value": 17, "children": []},
    5: {"value": 5, "children": []},
    6: {"value": 7, "children": []},
}


alpha = float('-inf')
beta = float('inf')

result = alpha_beta(0, alpha, beta, True)

print("Optimal value:", result)
