import pandas as pd
import math
import copy

data = {
    'Toothed': ['Toothed', 'Toothed', 'Toothed', 'Not Toothed', 'Toothed', 'Toothed', 'Toothed', 'Toothed', 'Toothed', 'Not Toothed'],
    'Hair': ['Hair', 'Hair', 'Not Hair', 'Hair', 'Hair', 'Hair', 'Not Hair', 'Not Hair', 'Not Hair', 'Not Hair'],
    'Breathes': ['Breathes', 'Breathes', 'Breathes', 'Breathes', 'Breathes', 'Breathes', 'Not Breathes', 'Breathes', 'Breathes', 'Breathes'],
    'Legs': ['Legs', 'Legs', 'Not Legs', 'Legs', 'Legs', 'Legs', 'Not Legs', 'Not Legs', 'Legs', 'Legs'],
    'Species': ['Mammal', 'Mammal', 'Reptile', 'Mammal', 'Mammal', 'Mammal', 'Reptile', 'Reptile', 'Mammal', 'Reptile']
}

attribute = ['Toothed', 'Hair', 'Breathes', 'Legs']


class Node(object):
    def __init__(self):
        self.value = None
        self.decision = None
        self.childs = None


def find_entropy(data, rows):
    yes = sum(1 for i in rows if data['Species'][i] == 'Mammal')
    no = sum(1 for i in rows if data['Species'][i] == 'Reptile')
    entropy = 0

    if yes != 0 and no != 0:
        x = yes / (yes + no)
        y = no / (yes + no)
        entropy = -1 * (x * math.log2(x) + y * math.log2(y))

    return entropy


def find_max_gain(data, rows, columns):
    max_gain = 0
    ret_idx = -1
    entropy = find_entropy(data, rows)

    if entropy == 0:
        return max_gain, ret_idx

    for j in columns:
        my_dict = {}
        idx = j
        for i in rows:
            key = data[attribute[idx]][i]
            if key not in my_dict:
                my_dict[key] = 1
            else:
                my_dict[key] += 1

        gain = entropy

        for key in my_dict:
            yes = sum(1 for k in rows if data['Species'][k] == 'Mammal' and data[attribute[idx]][k] == key)
            no = sum(1 for k in rows if data['Species'][k] == 'Reptile' and data[attribute[idx]][k] == key)

            x = yes / (yes + no)
            y = no / (yes + no)

            if x != 0 and y != 0:
                gain += (my_dict[key] * (x * math.log2(x) + y * math.log2(y))) / len(rows)

        if gain > max_gain:
            max_gain = gain
            ret_idx = j

    return max_gain, ret_idx


def build_tree(data, rows, columns):
    max_gain, idx = find_max_gain(data, rows, columns)
    root = Node()
    root.childs = []

    if max_gain == 0:
        root.value = 'Mammal' if sum(1 for i in rows if data['Species'][i] == 'Mammal') > 0 else 'Reptile'
        return root

    root.value = attribute[idx]
    my_dict = {}
    for i in rows:
        key = data[attribute[idx]][i]
        if key not in my_dict:
            my_dict[key] = 1
        else:
            my_dict[key] += 1

    new_columns = copy.deepcopy(columns)
    new_columns.remove(idx)

    for key in my_dict:
        new_rows = [i for i in rows if data[attribute[idx]][i] == key]
        temp = build_tree(data, new_rows, new_columns)
        temp.decision = key
        root.childs.append(temp)

    return root


def traverse(root):
    print(root.decision)
    print(root.value)

    n = len(root.childs)
    if n > 0:
        for i in range(0, n):
            traverse(root.childs[i])


def predict_new_example(new_example, root):
    current_node = root

    while current_node.childs:
        attribute_value = new_example[current_node.value]
        child_node = None

        for child in current_node.childs:
            if child.decision == attribute_value:
                child_node = child
                break

        if child_node:
            current_node = child_node
        else:
            break

    return current_node.value


def calculate():
    rows = [i for i in range(len(data['Toothed']))]
    columns = [i for i in range(len(attribute))]
    root = build_tree(data, rows, columns)
    root.decision = 'Start'

    new_example = {
        'Toothed': 'Toothed',
        'Hair': 'Hair',
        'Breathes': 'Not Breathes',
        'Legs': 'Legs'
    }

    predicted_species = predict_new_example(new_example, root)
    print(f"Predicted species: {predicted_species}")


calculate()
