'''
http://community.topcoder.com/stat?c=problem_statement&pm=13688
'''
def f(index):
    '''
    f(index) = number of ways to fill empty places in a[index...(n-1)]
    '''
    global a, n, dp
    if index == n:
        dp[index] = 1
        return 1
    else:
        res = 0
        if a[index] == 0:
            for j in range(1, len(a[index:])+1):
                valid = True
                for k in range(index, index+j):
                    if a[k] != 0 and a[k] != j:
                        valid = False
                        break
                if valid == True:
                    res += f(index + j)
                    #if res > 1:
                    #    res = 2
        # a[index] != 0
        else:
            j = a[index]
            if (index + j) <= n:
                valid = True
                for k in range(index, index+j):
                    if a[k] != j:
                        valid = False
                        break
                if valid == True:
                    res = f(index + j)
                    #if res > 1:
                    #    res = 2

        dp[index] = res
        return res


if __name__ == '__main__':
    a = [0, 0]
    n = len(a)
    dp = [None for i in range(n+1)]
    res = f(0)
    if res == 1:
        print("Sufficient")
    else:
        print("Not Sufficient")
    