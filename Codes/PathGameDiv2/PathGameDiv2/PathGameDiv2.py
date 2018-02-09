'''
'''
if __name__ == "__main__":
    neg = -999999999999
    board = ["....#.##.....#..........."
            ,"..#......#.......#..#...."]

    n = len(board[0])
    dp = [[0 for i in range(n)] for i in range(2)]
    # base case
    if board[0][0] == '#' or board[1][0] == '#':
        pass
    else:
        dp[0][0] = dp[1][0] = 1
    
    for j in range(1,n):
        left = down = neg
        if board[0][j] == '.':
            # if we come from Left
            if board[0][j-1] == '.':
                left = (dp[0][j-1] + 1) if board[1][j] == '.' else dp[0][j-1]
            #if we come from Dowm 
            if board[1][j-1] == '.' and board[1][j] == '.':
                down = dp[1][j-1]
            dp[0][j] = max(left, down)
        
        left = up = neg
        if board[1][j] == '.':
            # if we come from Left
            if board[1][j-1] == '.':
                left = (dp[1][j-1] + 1) if board[0][j] == '.' else dp[1][j-1]
            # if we come from Up
            if board[0][j-1] == '.' and board[0][j] == '.':
                up = dp[0][j-1]
            dp[1][j] = max(left, up) 

    print(max(dp[0][n-1], dp[1][n-1]))