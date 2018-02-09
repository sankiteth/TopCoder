def main():
    #always convert s1 to s2
    #initially s1 shorter and s2 longer
    s1 = 'MART'
    s2 = 'KARMA'
    Ins = 1
    Del = 1
    Rep = 1
    if Del < Ins:
        #convert longer to shorter
        s1, s2 = s2, s1
    cost = [[0 for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    #base cases
    for i in range(len(s2) + 1):
        cost[0][i] = i*Ins
    for i in range(len(s1) + 1):
        cost[i][0] = i*Del

    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            cost[i][j] = min((cost[i-1][j-1] + (0 if s1[i-1]==s2[j-1] else Rep)),
                              cost[i][j-1] + Ins,
                              cost[i-1][j] + Del)
    print('Initially:')
    print(*cost,sep='\n')
    print('The minimum cost is {0}'.format(cost[len(s1)][len(s2)]))
    i, j = len(s1), len(s2)
    lst = []
    while(i>0):
        if cost[i][j] == cost[i-1][j-1] and s1[i-1]==s2[j-1]:
            lst.append('allign {0} with {1}'.format(s1[i-1],s2[j-1]))
            i, j = i-1, j-1
        else:
            minimum = min(cost[i-1][j-1],
                          cost[i][j-1],
                          cost[i-1][j])
            if minimum == cost[i-1][j-1]:
                lst.append('replace {0} with {1}'.format(s1[i-1],s2[j-1]))
                i, j = i-1, j-1
            elif minimum == cost[i][j-1]:
                lst.append('insert {0} after {1}'.format(s2[j-1],s1[i-1]))
                j = j-1
            else:
                lst.append('delete {0}'.format(s1[i-1]))
                i = i-1
    print('Converting {0} to {1}'.format(s1,s2))
    print(*lst,sep='\n')
if __name__=='__main__':
    main()