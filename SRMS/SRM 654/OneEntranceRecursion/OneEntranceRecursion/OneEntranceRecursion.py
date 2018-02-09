'''
http://community.topcoder.com/stat?c=problem_statement&pm=13698
f(tree, num) = number ofways to place "num" furnitures in "tree"
f(tree, num) = Sum {x belongs to leaves(tree)} ( f(tree-leaf(x), num-1) )

'''
from copy import deepcopy
#num is number of furnitures to be moved
def f(graph, isLeaf, num):
    global s
    if num == 1:
        return 1
    ret = 0
    for i in range(len(graph)):
        if len(graph[i]) != 0 and isLeaf[i] and i != s:
            newGraph = deepcopy(graph)
            newIsLeaf = deepcopy(isLeaf)
            newGraph[newGraph[i][0]].remove(i) 
            if len(newGraph[newGraph[i][0]]) == 1:
                newIsLeaf[newGraph[i][0]] = True
            newGraph[i] = []
            newIsLeaf[i] = []
            ret += f(newGraph, newIsLeaf, num-1)
    return ret


if __name__ == '__main__':
    a = [7, 4, 1, 0, 1, 1, 6, 0]
    b = [6, 6, 2, 5, 0, 3, 8, 4]
    s = 4

    N = len(a) + 1
    graph = [[] for i in range(N)]
    for i in range(N-1):
        graph[a[i]].append(b[i])
        graph[b[i]].append(a[i])
    
    isLeaf = [False for i in range(N)]
    for i in range(N):
        if len(graph[i]) == 1:
            isLeaf[i] = True

    num = f(deepcopy(graph), deepcopy(isLeaf), N)
    print(num)