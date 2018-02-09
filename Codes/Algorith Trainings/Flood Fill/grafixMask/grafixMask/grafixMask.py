'''
http://community.topcoder.com/stat?c=problem_statement&pm=2998&rd=5857
'''
import sys
sys.setrecursionlimit(240000)

from queue import Queue

def RectangleCheck(nodes):
    global rects
    res = []
    for node in nodes:
        flag = True
        for i in rects:
            if (i[0][0] <= node[0] <= i[1][0]) and (i[0][1] <= node[1] <= i[1][1]): # within rectangle
                flag = False
                break
        if flag == True:
            res.append(node)
    return res

def ValidNeighbours(node):
    global rows, cols
    res = []
    if 0<=(node[0])<rows:
        if 0<=(node[1]-1)<cols:
            nbr = (node[0], node[1]-1)
            res.append(nbr)
        if 0<=(node[1]+1)<cols:
            nbr = (node[0], node[1]+1)
            res.append(nbr)

    if 0<=(node[1])<cols:
        if 0<=(node[0]-1)<rows:
            nbr = (node[0]-1, node[1])
            res.append(nbr)
        if 0<=(node[0]+1)<rows:
            nbr = (node[0]+1, node[1])
            res.append(nbr)

    # diagonal neighbours
    if 0<=(node[0]-1)<rows:
        if 0<=(node[1]-1)<cols:
            nbr = (node[0]-1, node[1]-1)
            res.append(nbr)
        if 0<=(node[1]+1)<cols:
            nbr = (node[0]-1, node[1]+1)
            res.append(nbr)

    if 0<=(node[0]+1)<rows:
        if 0<=(node[1]-1)<cols:
            nbr = (node[0]+1, node[1]-1)
            res.append(nbr)
        if 0<=(node[1]+1)<cols:
            nbr = (node[0]+1, node[1]+1)
            res.append(nbr)

    res = RectangleCheck(res)
    return res

# DFS
#def Traverse(node):
#    global maze, numNodes
#    maze[node[0]][node[1]] = True
#    for nbr in ValidNeighbours(node):
#        #if nbr not in visited:
#        if maze[nbr[0]][nbr[1]] == False:
#            numNodes += 1
#            Traverse(nbr)

def Traverse(node):
    '''
    BFS 
    '''
    global que, maze, numNodes
    que.put(node)
    maze[node[0]][node[1]] = True

    while(not que.empty()):
        item = que.get()
        for nbr in ValidNeighbours(item):
            if maze[nbr[0]][nbr[1]] == False:
                numNodes += 1
                que.put(nbr)
                maze[nbr[0]][nbr[1]] = True

if __name__ == '__main__':
    rows = 400
    cols = 600
    rectangles = ["0 192 399 207", "0 392 399 407", "120 0 135 599", "260 0 275 599"]

    rects = []
    for i in rectangles:
        arr = i.split(" ")
        topLeft = (int(arr[0]), int(arr[1]))
        bottomRight = (int(arr[2]), int(arr[3]))
        rects.append((topLeft, bottomRight))

    print(*rects, sep='\n')
    maze = []
    for i in range(400):
        maze.append([])
        for j in range(600):
            maze[i].append(False)
    
    que = Queue()
    holes = []
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == False:
                numNodes = 0
                Traverse((row, col))
                if numNodes > 0:
                    holes.append(numNodes)
    
    holes.sort()
    print(*holes,sep='\n')
