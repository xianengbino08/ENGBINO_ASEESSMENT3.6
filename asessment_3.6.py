class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(
    'X',
    left=Node(
        'I',
        left=Node(
            'A',
            left=Node('N', left=Node('E')),
            right=Node('N')
        ),
        right=Node('G', right=Node('B'))
    ),
    right=Node(
        'I',
        left=Node('N', left=Node('O'))
    )
)


def print_tree(node, prefix="", is_last=True):
    if node is None:
        return
    connector = "└── " if is_last else "├── "
    print(prefix + connector + str(node.val))
    children = [child for child in (node.left, node.right) if child is not None]
    for i, child in enumerate(children):
        child_is_last = (i == len(children) - 1)
        extension = "    " if is_last else "│   "
        print_tree(child, prefix + extension, child_is_last)


def preorder(node):
    if node is None:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]


print("PREORDER: ", " ".join(preorder(root)))
print("INORDER:  ", " ".join(inorder(root)))
print("POSTORDER:", " ".join(postorder(root)))