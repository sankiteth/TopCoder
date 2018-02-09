'''
http://community.topcoder.com/stat?c=problem_statement&pm=13504&rd=16080
'''
if __name__ == '__main__':
    hand = [6,12,17,14,20,8,16,7,2,15]
    sothe = [-1,-1,4,-1,11,3,13,-1,-1,18]

    n = len(hand)
    known = [x for x in sothe if x != -1]
    unknown = [x for x in range(1,2*n+1) if x not in hand and x not in sothe]
    hand = sorted(hand)
    known = sorted(known)
    bad = [] # for every element 'x' in 'known', we find the first element in 'hand' 'y' larger than x. All elements in 
    # 'hand' which are smaller than x are put in 'bad'. After doing this for all elements in 'known', if anything is left
    # in hand, put them in bad, so that we can pull off some wins for elements in 'unknown'
    score = 0

    for x in known:
        # all elements in hand smaller than x appended to 'bad' 
        while (len(hand) > 0) and (hand[0] <= x):
            bad.append(hand[0])
            hand = hand[1:]
        # first element in hand greater than x. Increase score by 1
        if len(hand) > 0:
            score += 1
            hand = hand[1:]
        # no element in hand greater than x. Assign the smallest element in hand(which is in bad now) to x
        else:
            if len(bad) > 0:
                bad = bad[1:]
    # Everything left in 'hand' is added to 'bad' to allign them with elements in 'unknown'
    for x in hand:
        bad.append(x)

        '''
        Lineraity of Expectation:
        The expected value of the sum of scores = The sum of expected values of each score
        Any of the possible permutations of 'unknown' cards could be alligned with cards in 'bad'
        We need to find the expected value of the sum of the individual scores of each card.
        By Lenearity of Expectation, that is eqivalent to "finding the sum of the expected values of the score of each 
        individual card"
        '''
    for x in bad:
         good = sum( y < x for y in unknown )
         score += good / float(len(unknown))
    
    print(score)



