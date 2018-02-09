def BuildZArray(str):
    length = len(str)
    L = R = k = 0
    Z = [-1 for i in range(length)]
    for i in range(1, length):
        if i > R:
            L = R = i
            while R < length and (str[R-L] == str[R]):
                R = R + 1

            Z[i] = R - L
            R = R - 1
        else:
            k = i - L
            if Z[k] < (R - i + 1):
                Z[i] = Z[k]
            elif Z[k] > (R - i + 1):
                Z[i] = R - i + 1
            else:
                L = i
                while R < length and (str[R-L] == str[R]):
                    R = R + 1
                Z[i] = R - L
                R = R - 1
    return Z

def ZSearch(text, pattern):
    concatStr = pattern + "$" + text
    length = len(concatStr)
    zArray = BuildZArray(concatStr)

    for i in range(length):
        if zArray[i] == len(pattern):
            print("Pattern found at index {0}".format(i - len(pattern) - 1))


if __name__ == '__main__':
    #text = "GEEKS FOR GEEKS"
    text = "abababaccca"
    pattern = "ababa"
    ZSearch(text, pattern)
