'''
Given two strings, figure out if 2nd one is substring of 1st one. 2nd may contain wildcard characters
'''
def PreProcess(search, posList):
    prefix = [0 for index in range(len(search))]
    i, j = 1, 0
    while(i < len(search)):
        if (search[i] == search[j]) or search[j] == '*' or search[i] == '*':
            prefix[i] = j + 1
            i = i + 1
            j = j + 1
        else:
            if j == 0:
                prefix[i] = 0
                i = i + 1
            else:
                prevJ = j
                j = prefix[j-1]
                #adjustment for wild card
                shift = prevJ - j
                pos = 0
                flag = False
                while(pos < len(posList)):
                    if (posList[pos] >= prevJ-j) and (posList[pos] <= prevJ-1):
                        index = (i-j) + (posList[pos]-shift) # (i-j) gives starting index of comparison in 'i'
                        if (search[posList[pos]-shift] == search[index]) or search[index] == '*':
                            pass
                        else:
                            prevJ = j
                            j = prefix[j-1]
                            shift = prevJ - j
                            flag = True

                    if flag == True:
                        pos = 0
                        flag = False
                    else:
                        pos = pos + 1
    return prefix

def main():
    text = 'abcabcabcabc'
    search = 'abc***abc'
    wildCardPosList = [2, 3, 6]
    #longest prefix which is also a suffix
    prefix = PreProcess(search, wildCardPosList)
    print('Prefix Array is:')
    print(*prefix, sep=',')
    i, j = 0, 0
    start = 0
    while(i < len(text)):
        if (text[i] == search[j]) or (search[j] == '*'):
            if j == len(search) - 1:
                print('Match found at position {0}'.format(start))
                j = prefix[j]
                i = i + 1
                start = i - j
            else:
                i = i + 1
                j = j + 1
        else:
            if j == 0:
                i = i + 1
                start = i
            else:
                j = prefix[j-1]
                start = i - j

if __name__ == '__main__':
    main()