def change(lst,x):
    lst = [0]*5
    for i in range(5):
       lst[i]=1
    x = 'In Change func'
    print(x)
    print(*lst,sep=' ')

if __name__ == '__main__':
    lst = [0]*5
    x='In main func'
    print(x)
    print(*lst,sep=' ')

    change(lst,x)

    print(x)
    print(*lst,sep=' ')