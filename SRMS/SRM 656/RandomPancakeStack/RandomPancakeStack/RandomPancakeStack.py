'''
http://community.topcoder.com/stat?c=problem_statement&pm=13747
E(top, cur) = Expected value of remaining choices when stack contains pancake "top" on top and has already "cur" pancakes in stack
'''



def E(top, cur):
    global d, N
    if dp[top][cur] != None:
        return dp[top][cur]
    elif top == 0:
        dp[top][cur] = 0
        return 0
    else:
        exp = 0
        for i in range(0, top):
            exp += ((1 / (N - cur) ) * (E(i, cur+1) + d[i] ) )
        dp[top][cur] = exp
        return exp

if __name__ == '__main__':
    d = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    N = len(d)
    dp = [[None for j in range(N+1)] for i in range(N+1)]
    res = E(N, 0)
    print(res)