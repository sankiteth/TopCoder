'''
Find LCA of two nodes in a Binary Tree.
Solve the problem by reducing it to Range Minimum Query (RMQ) Problem.
O(n) time for pre-processing and O(log n) time for RMQ 
'''
import math

class Node:
    #Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

#Recursive version of the Euler tour of Tree
def eulerTour(root, height):
    #if the passed node exists
    if root:
        global ind
        euler[ind] = root.key
        level[ind] = height
        ind += 1

        if firstOccurrence[root.key] == -1:
            firstOccurrence[root.key] = ind-1

        if root.left:
            eulerTour(root.left, height+1)
            euler[ind] = root.key
            level[ind] = height
            ind += 1

        if root.right:
            eulerTour(root.right, height+1)
            euler[ind] = root.key
            level[ind] = height
            ind += 1

#A recursive function that constructs Segment Tree (of indices) for array[startIndex..endIndex].
#currentIndex is index of current node in segment tree st
def constructSegmentTreeUtil(currentIndex, startIndex, endIndex, arr, st):
    #If there is one element in array, store it in current node of
    #segment tree and return
    if startIndex == endIndex:
        st[currentIndex] = startIndex
    else:
        #If there are more than one elements, then recur for left and
        #right subtrees and store the minimum of two values in this node
        mid = (startIndex + endIndex)//2
        constructSegmentTreeUtil(currentIndex*2+1, startIndex, mid, arr, st)
        constructSegmentTreeUtil(currentIndex*2+2, mid+1, endIndex, arr, st)
 
        if arr[st[2*currentIndex+1]] < arr[st[2*currentIndex+2]]:
            st[currentIndex] = st[2*currentIndex+1]
        else:
            st[currentIndex] = st[2*currentIndex+2]

#Function to construct segment tree from given array. This function
#allocates memory for segment tree and calls constructSegmentTreeUtil() to
#fill the allocated memory
def constructSegmentTree(arr, numOfLeafNodes):
    #Height of Segment Tree
    heightSt = int(math.log2(numOfLeafNodes)) + 1

    #Maximum size of segment tree
    max_size = 2*(1 << heightSt) - 1  #  2*pow(2,heightSt) -1

    #Number of nodes in segment tree is (2*V - 1)
    st = [-1 for i in range(0, max_size)]

    #Fill the tree st
    constructSegmentTreeUtil(0, 0, numOfLeafNodes-1, arr, st)
    return st

def RMQUtil(currentIndex, segmentStart, segmentEnd, queryStart, queryEnd, st):
    #If segment of this node is a part of given range, then return
    #the min of the segment
    if (queryStart <= segmentStart and queryEnd >= segmentEnd):
        return st[currentIndex]
    #If segment of this node is outside the given range
    elif (segmentEnd < queryStart or segmentStart > queryEnd):
        return -1

    #If a part of this segment overlaps with the given range
    mid = (segmentStart + segmentEnd)//2

    minLeft = RMQUtil(2*currentIndex+1, segmentStart, mid, queryStart, queryEnd, st)
    minRight = RMQUtil(2*currentIndex+2, mid+1, segmentEnd, queryStart, queryEnd, st)

    if minLeft == -1:
        return minRight
    elif minRight == -1:
        return minLeft

    return minLeft if level[minLeft] < level[minRight]  else minRight 

#Return minimum of elements in range from index queyStart to queryEnd
def RMQ(st, numOfNodes, queryStart, queryEnd):
    #Return minimum of elements in range from index queyStart to queryEnd
    #Check for erroneous input values
    if (queryStart < 0 or queryEnd > numOfNodes-1 or queryStart > queryEnd):
        print('Invalid Input')
        return -1
 
    return RMQUtil(0, 0, numOfNodes-1, queryStart, queryEnd, st)

#Returns LCA of nodes val1, val2 (assuming they are present in the tree)
def findLca(root, val1, val2):
    global V
    height = 0

    #Start Euler tour with root node on level 0
    eulerTour(root, height)

    #construct segment tree of indices of level array
    st = constructSegmentTree(level, 2*V-1)

    #If val2 before val1 in Euler tour.  For RMQ to work, first
    #parameter 'val1' must be smaller than second 'val2'
    if firstOccurrence[val1] > firstOccurrence[val2]:
        val1, val2 = val2, val1

    queryStart = firstOccurrence[val1]
    queryEnd = firstOccurrence[val2]

    #query for index of LCA in tour
    index = RMQ(st, 2*V-1, queryStart, queryEnd)
 
    #return LCA node
    return euler[index]

if __name__ == '__main__':
    V = 9
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)

    #First occurences of nodes in tour
    firstOccurrence = [-1 for i in range(0, V+1)] 
    
    #Variable to fill-in euler and level arrays
    ind = 0

    #For Euler tour sequence
    euler = [-1 for i in range(0, 2*V)]

    #Level of nodes in tour sequence
    level = [-1 for i in range(0, 2*V)]

    u = 4
    v = 9

    lca = findLca(root, u, v)
    print('The LCA of {} and {} is {}'.format(u, v, lca))