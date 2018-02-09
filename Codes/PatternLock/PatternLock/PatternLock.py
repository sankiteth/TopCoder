import copy
from _functools import reduce

def FindNbrs(G, cur):
    '''
    Finds neighbours of node 'cur' in graph 'G' having no. of nodes 'nodes' 
    '''
    nbrs = []
    for j in range(2*N):
        if G[cur][j] == 1:
            nbrs.append(j)
    return nbrs

def FindPaths(G, nodes, cur, traversed):
    '''
    Finds number of paths having "nodes" distinct nodes in graph 'G' starting at node 'cur'
    '''
    if nodes == 2:
        return 1
    nbrs = FindNbrs(G, cur)
    numPaths = 0
    GCopy = copy.deepcopy(G)
    traversed[cur] = True
    for j in nbrs:
        GCopy[cur][j] = GCopy[j][cur] = 0
    if cur!=0 and cur!=N and cur!=N-1 and cur!=2*N-1:# i.e. 'cur' is not a corner node
        if traversed[cur-1] == True or traversed[cur+1] == True:
            pass
        else:
            GCopy[cur-1][cur+1] = GCopy[cur+1][cur-1] = 1
    for j in nbrs:
        numPaths = ( numPaths + FindPaths(GCopy, nodes-1, j, traversed) ) % MOD
    #G = GCopy
    traversed[cur] = False
    return numPaths

def main():
    G = [[0 for i in range(2*N)] for i in range(2*N)]
    for i in range(N):
        for j in range(N,2*N):
            G[i][j] = 1
            G[j][i] = 1
        if N > 1:
            if i==0:
                G[i][i+1] = 1
                G[i+N][i+N+1] = 1
            elif i==N-1:
                G[i][i-1] = 1
                G[i+N][i+N-1] = 1
            else:
                G[i][i+1] = G[i][i-1] = 1
                G[i+N][i+N+1] = G[i+N][i+N-1] = 1
    
    #print('G:')
    #print(*G,sep='\n')
    paths = [0 for i in range(2*N)]#path[i] contains path of length '2*N' distinct nodes starting at node 'i' 
    traversed = [False for i in range(2*N)]#traversed[i] contains whether node'i' is already part of the path 
    for i in range(2*N):
        paths[i] = FindPaths(G, 2*N, i, traversed)
    #print('paths:')
    #print(*paths,sep=',')

    print('Total num of paths={0}'.format( reduce( ( lambda x, y: (x + y)%MOD ), paths) ) )

if __name__=='__main__':
    N = 4
    MOD = 1000000007

    main()