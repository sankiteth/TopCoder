'''
http://apps.topcoder.com/wiki/display/tc/SRM+654
To know the value contributed by each element to the final sum you only need to know the current amount of open brackets. 
At any step, we can either open a bracket or close a bracket or simply move on.
'''

def f(index, open, remaining):
    '''
    f(index, open, remaining) = sum value of all elements with index greater than or equal to 'index', such that
    there are currently 'open' open brackets and we can add 'remaining' more brackets.
    '''
    global n, a
    if dp[index][open][remaining] != None:
        res = dp[index][open][remaining]
    else:
        if index == n:
            #reached end of sequence-close all open parenthesis
            res = 0
        else:
            res = -999999999
            #x is sign of a[index] after evaluation of parenthesis
            x = -a[index] if (open % 2 == 0) else a[index]
            if remaining > 0:
                #can open 1 parenthesis
                res = max(res, x + f(index+1, open+1, remaining-1) )
            if open > 0:
                #can close it, we close the parenthesis BEFORE the element
                res = max(res, f(index, open-1, remaining) )
            #do nothing, just move ahead in sequence
            res = max(res, x + f(index+1, open, remaining))
        dp[index][open][remaining] = res
    return res

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    p = [1, 2, 0, 4, 3]
    v = [3, 9, -10, 5, 1]

    r = [None for i in range(len(p))]
    n = len(a)
    for i in range(len(p)):
        a[p[i]] = v[i]
        dp = [[[None for k in range(3)] for j in range(3)] for i in range(n+1)]
        r[i] = a[0] + f(1, 0, 2)
    print(r,sep=',')
