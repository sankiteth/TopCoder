'''
http://community.topcoder.com/stat?c=problem_statement&pm=13369
'''
from copy import deepcopy

def f(arr, k):
    if tuple(arr) in dp[k]:
        return dp[k][tuple(arr)]
    else:
        res = 0
        #base case
        if k == 0:
            res = 1
        else:
            arr1 = deepcopy(arr)
            for i in range(n-1,0,-1):
                for j in range(n-2,-1,-1):
                    if j != arr1[i-1] and j != i:
                        arr1[i-1] = j
                        res = f(arr1, k-1)
        dp[k][tuple(arr)] = res
        return res

def main():
    pass

if __name__ == '__main__':
    p = [0, 1, 2, 2, 0]
    arr = deepcopy(p)
    n = len(p)+1
    nbr = [[] for i in range(n)]
    for i in range(len(p)):
        nbr[p[i]].append(i+1)
        nbr[i+1].append([i])
    k = 2
    dp = dict()
    for i in range(1,k+1):
        dp[i] = {}
    num = f(arr, k)
    main()