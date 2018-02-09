'''
incremental AP = an AP with common diff 1
http://community.topcoder.com/stat?c=problem_statement&pm=13389&rd=16075
'''
def subString(dp):
    for i in range(len(dp)):
        for j in range(i,len(dp)):
            yield dp[i][j]

def main():
    d = [0,100,0,2,0]
    n = len(d)
    dp = [[0 for i in range(n)] for i in range(n)]
    #base case
    for i in range(n):
        #AP ending in odd number
        if d[i] == 0:
            dp[i][i] = 1
        #AP ending in even number
        else:
            dp[i][i] = 2
    for l in range(2, n+1):
        for i in range(n+1-l):
            j = i+l-1
            if l == 2:
                if (d[i] == 0 and d[j] != 0) or (d[i] != 0 and d[j] == 0):
                    dp[i][j] = (1 if d[j] == 0 else 2)
                else:
                    dp[i][j] = 0
            else:
                #(i=>j-1) is not AP
                if dp[i][j-1] == 0:
                    dp[i][j] = 0
                #(i=>j-1) is in AP ending in odd number
                elif dp[i][j-1] == 1:
                    if (d[j-2] == 1 and d[j] != 1) or (d[j-2] != 1 and d[j] == 1): 
                        dp[i][j] = 2
                #(i=>j-1) is in AP ending in even number
                elif dp[i][j-1] == 2:
                    if d[j] == 0:
                        dp[i][j] = 1
    print(*dp,sep='\n')
    print(sum(i!=0 for i in subString(dp)))

if __name__ == '__main__':
    main()