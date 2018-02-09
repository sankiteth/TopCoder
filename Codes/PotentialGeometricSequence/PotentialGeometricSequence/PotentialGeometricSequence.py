'''
http://apps.topcoder.com/wiki/display/tc/SRM+632
'''
def Substrings(d):
    for j in range(len(d)+1):
        for i in range(j):
            yield d[i:j]
 
def IsArithmetic(s):
    if len(s) <= 1:
        return True
    d = s[1] - s[0]
    return all( (s[i] - s[i-1] == d) for i in range(1, len(s) ) )


def main():
    print(sum( IsArithmetic(s) for s in Substrings(d) ))

if __name__=='__main__':
    d = [1,3,5,5,5,5,64,4,23,2,3,4,5,4,3]
    main()