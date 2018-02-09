def main():
    N = 500
    MOD = 1000000007
    dp = [[None for i in range(N+1)] for i in range(N+1)]
    dp[0][0] = 1
    for y in range(1,N+1):
        dp[0][y] = 0
    #print('Intially dp:')
    #print(*dp,sep='\n')
    
    for i in range(1, N+1): 
        l = i
        y = 0
        x = i
        while l > 0:
            a = (x * dp[y][x-1]) % MOD
            b = ((2 * dp[x - 1][y]) % MOD) if x > 1 else 0
            dp[x][y] = (a + b) % MOD
            l = l - 1
            x = x - 1
            y = y + 1
    for j in range(1, N+1):
        l = N-j+1
        y = j
        x = N
        while l > 0:
            a = (x * dp[y][x-1]) % MOD
            b = ((2 * dp[x - 1][y]) % MOD) if x > 1 else 0
            dp[x][y] = (a + b) % MOD
            l = l - 1
            x = x - 1
            y = y + 1

    #print('Finally dp:')
    #print(*dp,sep='\n')
    numPaths = (2*dp[N][N]) % MOD
    print('Num of possible patterns={0}'.format(numPaths))

if __name__ == '__main__':
    main()