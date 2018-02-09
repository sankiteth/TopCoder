'''
http://community.topcoder.com/stat?c=problem_statement&pm=1861&rd=4630
'''

def Shorter(s1, s2):
    '''
    returns the shorter of the two string, or the lexicograpgically first
    '''
    if len(s1) == len(s2):
        if s1 <= s2:
            return s1
        else:
            return s2
    else:
        if len(s1) < len(s2):
            return s1
        else:
            return s2

def IsPalindrome(s):
    start = 0
    end = len(s)-1
    flag = True
    while(start < end):
        if s[start] == s[end]:
            start +=1
            end -= 1
        else:
            flag = False
            break
    return flag

def f(start, end):
    global base, dp
    subString = base[start:end+1]
    l = len(subString)

    res = ""
    if dp[start][end] != -1:
        return dp[start][end]

    elif IsPalindrome(subString):
        res = subString

    else:
        if subString[0] == subString[l-1]:
            res = subString[0] + f(start+1, end-1) + subString[l-1]
        else:
            res = Shorter(subString[0] + f(start+1,end) + subString[0], subString[l-1] + f(start, end-1) + subString[l-1] )

    dp[start][end] = res
    return res

if __name__ == '__main__':
    base = "ALRCAGOEUAOEURGCOEUOOIGFA"
    length = len(base)
    dp = [[-1 for j in range(length)] for i in range(length)]
    res = f(0, length-1)

    print(res)
    
