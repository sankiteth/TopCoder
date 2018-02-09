'''
Given an undirected graph G having positive weights and N vertices. 
You start with having a sum of M money. For passing through a vertex i, you must pay S[i] money. 
If you don't have enough money - you can't pass through that vertex. Find the shortest path from vertex 1 to vertex N, 
respecting the above conditions; or state that such path doesn't exist. If there exist more than one path having the 
same length, then output the cheapest one. Restrictions: 1<N<=100 ; 0<=M<=100 ; for each i, 0<=S[i]<=100. 
'''

if __name__ == '__main__':
    G = [
        [0,1,2,0],
        [1,0,0,2],
        [2,0,0,1],
        [0,2,1,0]
        ]
    n = len(G)
    M = 20
    S = [0,12,8,5]
    INF = 999999

    visited = set() # [[False for j in range(M+1)] for i in range(n)]
    minim = [[INF for j in range(M+1)] for i in range(n)]

    minim[0][M] = 0

    while(True):
        minDist = (INF + 1)
        minState = ()
        for i in range(len(minim)):
            for j in range(len(minim[0])):
                if (i,j) not in visited:
                    if minDist > minim[i][j]:
                        minDist = minim[i][j]
                        minState = (i,j)
        if minDist == INF:
            break
        visited.add(minState)
        if len(visited) == n:
            break
        
        for nbr in Neighbours(minState[0]):
            if (minState[1]-S[nbr])>=0 and ( minim[nbr][minState[1]-S[nbr]]>(minim[minState[0]][minState[1]] + G[minState[0]][nbr]) ):
                minim[nbr][minState[1]-S[nbr]] = minim[minState[0]][minState[1]] + G[minState[0]][nbr]

    minValue = INF
    moneyLeft = -1
    for j in range(M+1):
        if minValue > minim[n-1][j]:
            minValue = minim[n-1][j]
            moneyLeft = j
        if minValue == minim[n-1][j]:
            if moneyLeft < j:
                moneyLeft = j

    if minValue == INF:
        print("No path exists")
    else:
        print("Shortest path has length {0} and money left is {1}".format(minValue, moneyLeft))