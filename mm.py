import math

def minimax(curDepth, nodeIndex, maxTurn, game_tree, targetDepth):
    if curDepth == targetDepth:
        return game_tree[nodeIndex]["value"]

    children = game_tree[nodeIndex]["children"]
    if maxTurn:
        eval_func = max
    else:
        eval_func = min

    result = float("-inf") if maxTurn else float("inf")

    for child in children:
        eval = minimax(curDepth + 1, child, not maxTurn, game_tree, targetDepth)
        result = eval_func(result, eval)

    return result

treeDepth = 2

game_tree = {
    0: {"value": 5, "children": [1, 2]},
    1: {"value": 5, "children": [3, 4]},
    2: {"value": 5, "children": [5, 6]},
    3: {"value": 5, "children": []},
    4: {"value": 17, "children": []},
    5: {"value": 5, "children": []},
    6: {"value": 7, "children": []},
}


best_move_value = minimax(0, 0, True, game_tree, treeDepth)
print("The optimal value is:", best_move_value)