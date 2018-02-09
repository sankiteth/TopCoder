def CountPaths(i, j, k, dir):
    global row, col
    if k == 0:
        #If direction is row, then we can reach here 
        #only if direction is row and row is 0.
        if dir == 0 and i == 0:
            return 1
 
        #If direction is column, then we can reach here 
        #only if direction is column and column is 0.
        if dir == 1 and j == 0:
            return 1
 
        return 0;

    #Base case along row
    if dir == 0 and i == 0:
        return 1
    if dir == 0 and j == 0:
        return 0

    #base case along column
    if dir == 1 and j == 0:
        return 1
    if dir == 1 and i == 0:
        return 0

    #If this subproblem is already evaluated
    if (dp[dir][k][i][j] != -1):
        return dp[dir][k][i][j]

    else:
        num = 0
        if dir == row:
            n1 = CountPaths(i, j-1, k, row)
            n2 = CountPaths(i, j-1, k-1, col)
            num = n1 + n2
            
        if dir == col:
            n1 = CountPaths(i-1, j, k, col)
            n2 = CountPaths(i-1, j, k-1, row)
            num = n1 + n2

        dp[dir][k][i][j] = num
        return num
    

if __name__ == '__main__':
    m = 3
    n = 3
    k = 2
    row = 0
    col = 1

    dp = [[[[-1 for columns in range(n)] for rows in range(m)] for k in range(k+1)] for dir in range(2)]

    print(*dp, sep = ';')

    n1 = CountPaths(m-1, n-1, k, row)
    n2 = CountPaths(m-1, n-1, k, col)

    print(*dp, sep = ';')

    num = n1 + n2

    print('Number of paths is {}'.format(num))
