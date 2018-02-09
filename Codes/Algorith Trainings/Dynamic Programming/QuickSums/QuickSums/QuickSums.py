'''
http://community.topcoder.com/stat?c=problem_statement&pm=2829&rd=5072
'''

def f(numbers, sum):
    if len(numbers) == 0:
        return 999999
    if int(numbers) == sum:
        return 0
    else:
        best = 99999
        res = 999999
        for i in range(len(numbers)-1, -1, -1):
            numVal = int(numbers[i:])
            if numVal <= sum:
                res = 1 + f(numbers[:i], sum-numVal)
                if res < best:
                    best = res
        return best

if __name__ == '__main__':
    numbers = "111"
    sum = 4
    minSums = f(numbers, sum)
    if minSums == 99999:
        print(-1)
    else:
        print(minSums)
