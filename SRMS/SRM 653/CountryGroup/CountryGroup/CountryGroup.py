'''
http://community.topcoder.com/stat?c=problem_statement&pm=13687
'''

def Validate(index):
    global a, N
    if (index + a[index] - 1) >= N:
        return False
    for i in range(index, index+a[index]):
        if a[i] != a[index]:
            return False
    return True

if __name__ == '__main__':
    a = [2,2,3,3,3]
    N = len(a)
    index = 0
    res = True
    countries = 0
    while index < N:
        if a[index] == 1:
            countries += 1
        else:
            r = Validate(index)
            if r == False:
                countries = -1
                break
            else:
                countries += 1
                index += (a[index] - 1)
        index += 1
    print(countries)