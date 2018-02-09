def main():
    s = ['a', 'b', 'c']
    n = len(s)
    for  i in range(1<<n):
        res = []
        for j in range(n):
            if i & (1<<j):#'j'th bit is set
                res.append(s[j])
        print(*res,sep=',')

if __name__=='__main__':
    main()