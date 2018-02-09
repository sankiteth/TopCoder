class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def VerticalOrderTraversal(node, hd):
    global map
    if node == None:
        return

    if hd in map:
        map[hd].append(node.value)
    else:
        map[hd] = [node.value]

    VerticalOrderTraversal(node.left, hd-1)
    VerticalOrderTraversal(node.right, hd+1)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    map = dict()
    VerticalOrderTraversal(root, 0)

    print("Vertical order traversal is:\n")
    for key in sorted(map.keys()):
        print(*map[key], sep=',')

