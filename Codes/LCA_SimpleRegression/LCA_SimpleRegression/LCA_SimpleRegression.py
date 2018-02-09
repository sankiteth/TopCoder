'''
O(n) solution to find LCA of two given values n1 and n2 in a Binary Tree
'''

# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(root, val1, val2):
    if root is None:
        return None

    if root.key == val1 or root.key == val2:
        return root

    leftLca = findLCA(root.left, val1, val2)
    rightLca = findLCA(root.right, val1, val2)

    if leftLca and rightLca:
        return root

    if leftLca is not None:
        return leftLca
    else:
        return rightLca

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    lca = findLCA(root, 4, 5).key
    print(lca)
