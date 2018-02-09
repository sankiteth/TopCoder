'''
In Morris Traversal of Binary Tree, we first create links to Inorder successor and print the data using these links, and finally revert the changes to restore original tree.
'''

#Represents a Binary Tree Node
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#DO an inorder traversal of the Binary Tree
def Inorder(root):
    if root:
        Inorder(root.left)
        print('data = {}\n'.format(root.data))
        Inorder(root.right)

def MorrisTraversal(root):
    print("Morris Traversal:\n")
    if root == None:
        return
    current = root
    while current != None:
        if current.left == None:
            print('data = {0}\n'.format(current.data))
            current = current.right
        else:
            #Find the inorder predecessor of current
            pre = current.left
            while pre.right != None and pre.right != current:
                pre = pre.right

            #Make current as right child of its inorder predecessor
            if pre.right == None:
                pre.right = current
                current = current.left
            #Revert the changes made in if part to restore the original tree i.e., fix the right child of predecssor
            else:
                pre.right = None
                print('data = {0}\n'.format(current.data))
                current = current.right

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    root.left.left  = TreeNode(4);
    root.left.right = TreeNode(5); 

    Inorder(root)

    MorrisTraversal(root)
