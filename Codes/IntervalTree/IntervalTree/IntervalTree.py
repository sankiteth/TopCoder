'''
Consider a situation where we have a set of intervals and we need following operations to be implemented efficiently. 
1) Add an interval
2) Remove an interval
3) Given an interval x, find if x overlaps with any of the existing intervals.

Interval Tree: The idea is to augment a self-balancing Binary Search Tree (BST) like Red Black Tree, AVL Tree, etc to maintain set of intervals so that all operations can be done in O(Logn) time.

Every node of Interval Tree stores following information.
a) i: An interval which is represented as a pair [low, high]
b) max: Maximum high value in subtree rooted with this node.

The low value of an interval is used as key to maintain order in BST. The insert and delete operations are same as insert and delete in self-balancing BST used.
'''

class Interval(object):
    def __init__(self, low, high):
        self.__low = low
        self.__high = high

    @property
    def low(self):
        return self.__low

    @property
    def high(self):
        return self.__high

#Represents an Interval Tree Node
class ITNode(object):
    def __init__(self, interval):
        self.max = interval.high
        self.interval = interval
        self.left = None
        self.right = None

#A utility function to insert a new Interval Search Tree Node
#This is similar to BST Insert.  Here the low value of interval
#is used tomaintain BST property
def Insert(root, interval):
    #Base case: Tree is empty, new node becomes root
    if root == None:
        return ITNode(interval)

    low = root.interval.low

    if interval.low < low:
        root.left = Insert(root.left, interval)
    else:
        root.right = Insert(root.right, interval)

    #Update the max value of this ancestor if needed
    if root.max < interval.high:
        root.max = interval.high

    return root

#DO an inorder traversal of the Interval Search Tree
def Inorder(root):
    if root:
        Inorder(root.left)
        print('[{} - {}], max = {}\n'.format(root.interval.low, root.interval.high, root.max))
        Inorder(root.right)

def Overlap(int1, int2):
    if int1.low < int2.high and int2.low < int1.high:
        return True
    else:
        return False

#Searches for interval in the Interval Tree
def SearchOverlap(root, interval):
    overlap = None
    if root:
        if Overlap(root.interval, interval):
            return root.interval
        
        if root.left and interval.low < root.left.max:
            overlap = SearchOverlap(root.left, interval)
        else:
            overlap = SearchOverlap(root.right, interval)
        
    return overlap
    
if __name__ == '__main__':
    #Create interval tree shown in above figure
    intervals = [(15, 20), (10, 30), (17, 19),
        (5, 20), (12, 15), (30, 40)]
    
    root = None
    for i in range(len(intervals)):
        root = Insert(root, Interval(*intervals[i]))

    print('Inorder traversal of constructed Interval Tree is\n')
    Inorder(root)

    newInterval = Interval(6, 7)

    print('\nSearching for interval [{} - {}]:'.format(newInterval.low, newInterval.high))

    overlapInt = SearchOverlap(root, newInterval)

    if overlapInt == None:
        print('Interval [{0} - {1}] does not overlap'.format(newInterval.low, newInterval.high))
    else:
        print('Interval [{0} - {1}] overlaps with [{2} - {3}]'.format(newInterval.low, newInterval.high, overlapInt.low, overlapInt.high))


