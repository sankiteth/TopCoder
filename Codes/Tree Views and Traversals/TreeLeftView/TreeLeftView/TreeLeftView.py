class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def LeftTraversal(node, level, maxLevel):
    if node is None:
        return maxLevel
    if level > maxLevel:
        maxLevel = level
        print(node.value)
    maxLevel = LeftTraversal(node.left, level + 1, maxLevel)
    maxLevel = LeftTraversal(node.right, level + 1, maxLevel)
    return maxLevel

def NumNodes(root):
    if root is None:
        return 0
    else:
        return NumNodes(root.left) + 1 + NumNodes(root.right)



if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    
    LeftTraversal(root, 0, -1)
    num = NumNodes(root)
    print(num)
