'''
http://community.topcoder.com/stat?c=problem_statement&pm=13686
'''

if __name__ == '__main__':
    card = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    score = 7
    mod = 1000000007
    n = len(card)
    dp = [[None for j in range(score+1)] for i in range(n+1)]
    # base cases
    # dp[0][j] = 0 for 1<=j<=score
    for j in range(1, score+1):
        dp[0][j] = 0

    # dp[i][0] = 2^(i-1) for 0<=i<=n
    val = 1
    for i in range(0, n+1):
        dp[i][0] = val
        val = (val * 2) % mod

    for i in range(1, n+1):
        for j in range(1, score+1):
            dp[i][j] = (dp[i-1][j-1] + ((dp[i-1][j]*2) % mod ) ) % mod

    print(dp[n][score])