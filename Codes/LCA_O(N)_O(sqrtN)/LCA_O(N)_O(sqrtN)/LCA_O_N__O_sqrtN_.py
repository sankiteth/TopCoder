'''
An <O(N), O(sqrt(N))> solution
Dividing our input into equal-sized parts proves to be an interesting way to solve the 
RMQ problem. This method can be adapted for the LCA problem as well. 
The idea is to split the tree in sqrt(H) parts, were H is the height of the tree. 
Thus, the first section will contain the levels numbered from 0 to sqrt(H) - 1, 
the second will contain the levels numbered from sqrt(H) to 2 * sqrt(H) - 1, and so on. 
'''

from math import *
from queue import *

def Print(tree, sons, level, height, parent, lca):
    print(*tree,sep=',')
    print(*sons,sep='\n')
    print(*level,sep=',')
    print('height={0}'.format(height))
    print(*parent,sep=',')
    print('LCA={0}'.format(lca))

def Height(tree, sons, level):
    q1 = Queue(maxsize=10)
    q1.put(0)
    level[0] = 0
    q2 = Queue(maxsize=10)
    height = -1
    while (not q1.empty()) or (not q2.empty()):
        height = height + 1
        if height % 2 == 0:
            while not q1.empty():
                temp = q1.get()
                level[temp] = height
                for index,value in enumerate(sons[temp]):
                    q2.put(value)
        if height % 2 == 1:
            while not q2.empty():
                temp = q2.get()
                level[temp] = height
                for index,value in enumerate(sons[temp]):
                    q1.put(value)
    return height

def DFS(node, tree, sons, level, parent, nr):
    if level[node] < nr:
        parent[node] = 0
    else:
        if (level[node] % nr) == 0:
            parent[node] = tree[node]
        else:
            parent[node] = parent[tree[node]]
    for son in sons[node]:
        DFS(son, tree, sons, level, parent, nr)

def DFSNonRecursive(tree, sons, level, parent, nr):
    '''
    if node is in first section, assign parent[node]=0
    else if node is in first layer of its section assign parent[node]=tree[node]
         else parent[node] = parent[tree[node]]
    '''
    for node,value in enumerate(tree):
        if level[node] < nr:
            parent[node] = 0
        else:
            if (level[node] % nr) == 0:
                parent[node] = tree[node]
            else:
                parent[node] = parent[tree[node]]

def LCA(tree, level, parent, node1, node2):
    #trace back ancestors of both nodes that are in the same section
    while(parent[node1] != parent[node2]):
        if level[node2] > level[node1]:
            node2 = parent[node2]
        else:
            node1 = parent[node1]
    #now trace back LCA after we have found the section in which it lies
    while(node1 != node2):
        if level[node2] > level[node1]:
            node2 = parent[node2]
        else:
            node1 = parent[node1]
    return node1

def main():
    tree = [-1, 0, 0, 0, 2, 2, 2, 5, 5, 6, 6, 9, 9]
    sons = [[0 for i in range(0)] for i in range(len(tree))]
    for i in range(1,len(tree)):
        sons[tree[i]].append(i)
    level = [-1 for i in range(len(tree))]
    height = Height(tree, sons, level)
    nr = ceil(sqrt(height))
    parent = [0 for i in range(len(tree))]
    DFSNonRecursive(tree, sons, level, parent, nr)
    lca = LCA(tree, level, parent, 2, 8)
    Print(tree, sons, level, height, parent, lca)

if __name__=='__main__':
    main()