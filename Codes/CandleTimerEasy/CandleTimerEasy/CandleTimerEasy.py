'''
http://apps.topcoder.com/wiki/display/tc/SRM+638
'''
def main():
    #edge from A[i] to B[i] having weight length[i]
    A = [0,0,0]
    B = [1,2,3]
    length = [1,2,3]
    n = len(A) + 1 #no. of nodes in a tree = no. of edges + 1
    nbrs = [[] for i in range(n)] #adjacency list to represent neighbours of each node in the tree
    w = [[INF for i in range(n)] for i in range(n)] 
    for i in range(n-1):
        length[i] = length[i] * 2 #so that len[i]//2 is always integer
        for j in range(2): #A[i] is neighbour of B[i] and B[i] is neighbour of A[i]. So doing twice
            nbrs[A[i]].append(B[i])
            w[A[i]][B[i]] = length[i]
            A[i], B[i] = B[i], A[i] #A[i] is neighbour of B[i] and B[i] is neighbour of A[i]. So doing twice
    
            leaves = []
    for i in range(n):
        if len(nbrs[i]) == 1:
            leaves.append(i)
    
    t = len(leaves) #no. of leaves in the given tree
    times = set()

    for mask in range(1, 1<<t): #all possible subsets of 'leaves' set, except empty subset
        dist = [INF for i in range(n)] #measures min distance of every node in the tree from the present leaves' subset
        Q = [] #queue used in Dijikstra
        parent = [-1 for i in range(n)] #while measuring min dist of every node in the tree from the present leaves' subset, parent[i] stores the predecessor of node 'i'

        for i in range(t):
            if mask & (1<<i): #'i'th bit in mask is set i.e. 'i'th leaf is in current leaves' subset
                u = leaves[i]
                dist[u] = 0 #setting dist of source node to '0' as in Dijikstra
                Q.append(u)

        mx = 0
        # farthest point is a node in the tree
        while(len(Q) > 0):
            #deque smallest dist node from Q
            s = 0
            for i in range(1, len(Q)):
                if dist[Q[i]] < dist[Q[s]]:
                    s = i
            x = Q[s]
            del Q[s]
            mx = max(mx, dist[x])

            for y in nbrs[x]:
                if dist[y] > dist[x] + w[x][y]:
                    parent[y] = x
                    dist[y] = dist[x] + w[x][y]
                    if y not in Q:
                        Q.append(y)
        #farthest point is within an edge which lies on a path between any two leaves in the leaves' subset itself
        for i in range(n-1):
            x = dist[A[i]]
            y = dist[B[i]]
            #Greater of the two always in x
            if x < y:
                x, y = y, x
            if parent[A[i]] != B[i] and parent[B[i]] != A[i]:
                if (x - y) <= length[i]:
                    # 0            u      len[i]
                    # |------------|--------|
                    # A                     B
                    # at time x, flame 1 is in A
                    # at time y, flame 2 is in B
                    # at time x, flame 2 is in u = len[i] - (x - y)
                    # they will meet at time x + u/2
                    u = (length[i] - (x - y))//2
                    mx = max(mx, (x + u))
        times.add(mx)

    print('No. of different times={0}'.format(len(times)))
    print('And they are:')
    print(*times,sep=',')
if __name__ =='__main__':
    INF = 1000000000
    main()