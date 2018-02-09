'''
http://apps.topcoder.com/wiki/display/tc/SRM+635
'''
def BinarySearch(lo, hi, f):
    while lo + 1< hi :
        ha = lo + (hi - lo)//2
        if f(ha) == True:
            lo = ha
        else:
            hi = ha
    return lo

if __name__ == '__main__':
    d = 1
    res = BinarySearch(0, d+1, lambda x: (d - x - x**2) >= 0)
    print(res)