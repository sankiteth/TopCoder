'''
http://community.topcoder.com/stat?c=problem_statement&pm=13685
'''
from math import fabs

def f(p, lastB):
    global pitch
    if dp[p][lastB] != -1:
        return dp[p][lastB]
    else:
        res = 0
        if p >= n:
            res = 0
        else:
            # Choose A
            res = int(fabs(pitch[p] - pitch[p-1]) ) + f(p+1, lastB)

            # Choose B
            b = 0
            # not chosen before
            if lastB == n:
                b = f(p+1, p-1)
            else:
                # chosen before, swap the sets
                b = int(fabs(pitch[p] - pitch[lastB]) ) + f(p+1, p-1)
            res = min(res, b)

        dp[p][lastB] = res
        return res

if __name__ == '__main__':
    pitch = [1,3,8,12,13]
    n = len(pitch)
    dp = [[-1 for j in range(n+1)] for i in range(n+1)]
    res = f(1, n)

    print(res)