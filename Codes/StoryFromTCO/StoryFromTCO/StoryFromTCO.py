'''
http://apps.topcoder.com/wiki/display/tc/SRM+635
'''

def minimumChanges(places, cutoff):
    n = len(places)
    goodPlaces = []
    badPlaces = []
    goodCutoff = []
    badCutoff = []
    goodAdded = []
    for i in range(n):
        if places[i] <= cutoff[i]:
            goodPlaces.append(places[i])
            goodCutoff.append(cutoff[i])
            goodAdded.append(False)
        else:
            badPlaces.append(places[i])
            badCutoff.append(cutoff[i])

    badPlaces.sort()
    badCutoff.sort()

    i = 0
    while(i < len(badPlaces)):
        if badPlaces[i] > badCutoff[i]:
            r = -1
            for j in range(len(goodPlaces)):
                if (not goodAdded[j] 
                    and goodPlaces[j] <= badCutoff[i]
                    and (r == -1 or
                         goodCutoff[r] < goodCuttoff[j]
                         )
                    ):
                    r = j
            if r == -1:
                return -1
            else:
                goodAdded[r] = True
                badPlaces.append(goodPlaces[r])
                badCutoff.append(goodCutoff[r])
                # again sort from 'i'th index till end
                badPlaces = badPlaces[:i] + sorted(badPlaces[i:])
                badCutoff = badCutoff[:i] + sorted(badCutoff[i:])
        else:
            i += 1
    return len(badPlaces)

if __name__ == '__main__':
    places = [20,100,500,50]
    cutoff = [7500,2250,150,24]
    k = minimumChanges(places, cutoff)
    print(k)