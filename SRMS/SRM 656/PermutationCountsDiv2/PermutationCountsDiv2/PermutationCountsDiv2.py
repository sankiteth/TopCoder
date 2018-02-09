'''
http://community.topcoder.com/stat?c=problem_statement&pm=13739
f(a, b) = Number of ways to solve the sub-problem made from interval of positions [a,b) (includes a, excludes b)
'''

def PascalTriangle(N):
    C = [[0 for j in range(N+1)] for i in range(N+1)]
    for i in range(0, N+1):
        C[i][0] = 1
        for j in range(1, i+1):
            C[i][j] = ( C[i-1][j] + C[i-1][j-1] ) % MOD

    return C

def f(a, b):
    global arr, C, N, MOD
    if dp[a][b] != None:
        return dp[a][b]
    else: 
        if (b - a) == 1 or (b - a) == 0:
            ret = 1
        else:
            ret = 0
            for i in range(a, b):
                if (arr[i] or i == (b-1) ) and ((i == a) or (not arr[i-1]) ):
                    p = f(a, i)
                    q = f(i+1, b)
                    ret += (p * q * C[b-a-1][i-a] ) % MOD
        dp[a][b] = ret
        return ret

if __name__ == '__main__':
    N = 9
    pos = [2,4,5]
    MOD = 1000000007
    arr = [False for i in range(N)]
    C = PascalTriangle(N)
    for i in pos:
        arr[i-1] = True
    dp = [[None for j in range(N+1)] for i in range(N+1)]
    res = f(0, N)
    print(res)