'''
http://apps.topcoder.com/wiki/display/tc/SRM+638
'''
def f(perm):
    t = len(perm)
    if t <= 1:
        return 1
    else:
        min = max = 0
        res = 0
        for i in range(1,t):
            if size[perm[min]] > size[perm[i]]:
                min = i
            if size[perm[max]] < size[perm[i]]:
                max = i
        #largest wolf can't move
        if size[perm[max]] + size[perm[min]] > maxSizeSum:
            left = perm[:max]
            right = perm[max+1:]
            res = (f(left) * f(right)) % MOD
        #smallest wolf can fit anywhere
        else:
            newPerm = perm
            del newPerm[min]
            res = (f(newPerm) * t) % MOD
        return res

if __name__=='__main__':
    size = [2,4,6,1,3,5]
    maxSizeSum = 8
    MOD = 1000000007
    n = len(size)
    perm = list(range(n))
    num = f(perm)
    print('No. of possible permutations={0}'.format(num))