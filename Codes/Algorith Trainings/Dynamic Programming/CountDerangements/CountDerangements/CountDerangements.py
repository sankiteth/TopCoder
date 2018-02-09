'''
A Derangement is a permutation of n elements, such that no element appears in its original position. 
For example, a derangement of {0, 1, 2, 3} is {2, 3, 1, 0}.
Given a number n, find total number of Derangements of a set of n elements.
'''

def CountDerangementRecurcive(n):
    if n == 1 or n == 0:
        return 0
    elif n == 2:
        return 1
    else:
        return (n-1)*( CountDerangementRecurcive(n-1) + CountDerangementRecurcive(n-2) )

def CountDerangementDP(n):

    DP = [-1 for i in range(n+1)]

    #Base cases
    DP[0] = DP[1] = 0
    DP[2] = 1

    for i in range(3, n+1):
        DP[i] = (i-1) * ( DP[i-1] + DP[i-2] )

    return DP[n]

if __name__ == '__main__':
    n = 50
    print('Recursive: Count of derangement for {} elements is {}'.format(n, CountDerangementRecurcive(n)))

    print('DP: Count of derangement for {} elements is {}'.format(n, CountDerangementDP(n)))
