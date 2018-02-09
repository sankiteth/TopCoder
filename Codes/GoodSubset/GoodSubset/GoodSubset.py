'''
http://apps.topcoder.com/wiki/display/tc/SRM+632
'''
def f(x, t):
    #key 'x' is already prsent in dictionary 'dp[t]'
    if x in dp[t]:
        return dp[t][x]
    else:
        res = 0
        #base case
        if t == 0:
            # empty subset always has product 1 (multiplicative identity)
            if x == 1:
                res = 1
            else:
                res = 0
        else:
            #include 't'th element in solution
            if x % d[t-1] == 0:
                res = res + f(x//d[t-1], t-1)
            # does not include 't'th element
            res = res + f(x, t-1)
        dp[t][x] = res
        return res

if __name__ == '__main__':
    MOD = 1000000007
    goodValue = 12
    d = [1,2,3,4,5,6,7,8,9,10,11,12]
    #a dictionary of dictionaries
    dp = dict()
    for i in range(len(d)+1):
        dp[i] = {}
    num = f(goodValue, len(d)) - (1 if goodValue==1 else 0)
    print('No of subsets with product {0}={1}'.format(goodValue, num))