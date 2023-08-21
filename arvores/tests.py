import random
from arvores.tree import BinarySearchTree

def random_tree(size):
    random.seed(77)
    values = random.sample(range(1, 1000), size)

    bst = BinarySearchTree()
    for v in values:
        bst.insert(v)

    return bst

def example_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)

    return tree

tree = example_tree()

tree.postorder_traversal()

tree.levelorder_traversal()

# items = [1, 3, 981, 510, 1000]
# for item in items:
#     r = bst.search(item)

#     if r is None:
#         print(item, "não encontrado")
#     else:
#         print(item, "encontrado")
