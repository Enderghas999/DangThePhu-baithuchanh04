class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(g, x):
    if g is None:
        return Node(x)
    if x < g.value:
        g.left = insert(g.left, x)
    elif x > g.value:
        g.right = insert(g.right, x)
    return g

def preorder(g):
    if g is None:
        return []
    return [g.value] + preorder(g.left) + preorder(g.right)

def inorder(g):
    if g is None:
        return []
    return inorder(g.left) + [g.value] + inorder(g.right)

def height(g):
    if g is None:
        return 0
    return 1 + max(height(g.left), height(g.right))

# TODO: viết postorder(g), ghép trái + phải + [g.value].
def postorder(g):                         #dong da them
    if g is None:
        return []
    return postorder(g.left) + postorder(g.right) + [g.value]
root = None
for x in [45, 15, 79]:
    root = insert(root, x)
print("Preorder :", preorder(root))        #dong da them
print("Inorder  :", inorder(root))
print("Postorder:", postorder(root))
print("Height   :", height(root))
# Sau TODO, gọi print(postorder(root)).
