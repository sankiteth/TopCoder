'''
http://community.topcoder.com/stat?c=problem_statement&pm=13659
'''

def f(N, K):
    global dp
    if dp[N][K] != -1:
        return dp[N][K]
    else:
        res = 0
        if N == 0:
            res = 0
        else:
            res = f(N-1, K) + 1
            for x in range(1, N):
                for y in range(K):
                    res = min(res, max(f(x, y), f(N-x, K-y-1) ) + 1 )
                
        dp[N][K] = res
        return res


if __name__ == '__main__':
    N = 45
    K = 5
    dp = [[-1 for j in range(K+1)] for i in range(N+1)]
    res = f(N,K)
    print(res)