'''
parent[i][j]=(2^j)th ancestor of node 'i'.
For finding LCA of two nodes 'p' and 'q' s.t. level[p]>level[q]
first find ancestor of 'p' in same level as in 'q' and then find the 
LCA of this parent of 'p' and 'q'  
'''
from queue import Queue
def PreProcess(tree, n, parent, lgN):
    #ancestor of 2^0=1 length is its own parent
    for i in range(len(tree)):
        parent[i][0] = tree[i]
    for j in range(1,lgN+1):
        for i in range(n):
            if parent[i][j-1] != -1:
                parent[i][j] = parent[parent[i][j-1]][j-1]
        if parent[i][j] == 0 or parent[i][j] == -1:
            return  

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

def LCA(tree, parent, level, p, q):
    '''
    Assume level[p] > level[q]
    First, find parent of 'p' lying in same level as in 'q'
    In 'parent' table we have: 1st, 2nd, 4th,... ,Log(level[p])th ancestor of 'p'
    level['2^j'th ancestor of 'p']=level[p]-2^j
    From parent table, find the first ancestor '2^i' of 'p' whose level is >= the level of 'q'
    Now, Divide the length between level[q] and level[ancestor '2^i' of 'p'] in a 
    similar manner.

    Second, We must observe that if p and q are on the same level in the tree 
    we can compute LCA(p, q) using a meta-binary search. 
    So, for every power j of 2 (between log(L[p]) and 0, in descending order), 
    if P[p][j] != P[q][j] then we know that LCA(p, q) is on a higher level 
    and we will continue searching for LCA(p = P[p][j], q = P[q][j]). 
    At the end, both p and q will have the same father, so return T[p]
    '''
    logP = 1
    #ceil(log(level[p]))
    while (1 << logP) < level[p]:
        logP=logP+1
    #we find the ancestor of node p situated on the same level with q using the values in parent
    for i in range(logP,-1,-1):
        level_ith_ancestor = (level[p] - (1<<i))
        if level_ith_ancestor >= level[q]:
            p = parent[p][i]
    if p == q:
        return p
    #we compute LCA(p, q) using the values in parent
    for i in range(logP,-1,-1):
        if (parent[p][i] != -1 and parent[p][i] != parent[q][i]):
              p,q = parent[p][i], parent[q][i]
    return tree[p]

def Print(tree, sons, level, height, parent, lca):
    print(*tree,sep=',')
    print(*sons,sep='\n')
    print(*level,sep=',')
    print('height={0}'.format(height))
    print(*parent,sep='\n')
    print('LCA={0}'.format(lca))

def main():
    tree = [-1, 0, 0, 0, 2, 2, 2, 5, 5, 6, 6, 9, 9, 10, 10, 10]
    n = len(tree)
    lgN = 0
    while (n-1>>lgN) > 0:
        lgN = lgN + 1
    parent = [[-1 for i in range(lgN+1)] for i in range(n)]
    PreProcess(tree, n, parent, lgN)

    sons = [[0 for i in range(0)] for i in range(len(tree))]
    for i in range(1,len(tree)):
        sons[tree[i]].append(i)
    level = [-1 for i in range(len(tree))]
    height = Height(tree, sons, level)
    lca = LCA(tree, parent, level, 14, 2)
    Print(tree, sons, level, height, parent, lca)

if __name__=='__main__':
    main()