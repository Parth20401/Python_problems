from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    #fall back to brute force solution
    pos = []
    neg = []
    n = len(a)

    for i in range(n):
        if a[i] > 0:
            pos.append(a[i])
        else:
            neg.append(a[i])

    # If positives are lesser than the negatives.
    if len(pos) < len(neg):
        # First, fill array alternatively till the point where positives and negatives are equal in number
        for i in range(len(pos)):
            a[2 * i] = pos[i]
            a[2 * i + 1] = neg[i]

        # Fill the remaining negatives at the end of the array.
        index = len(pos) * 2
        for i in range(len(neg) - len(pos)):
            a[index] = neg[len(pos) + i]
            index += 1

    # If negatives are lesser than the positives.
    else:
        for i in range(len(neg)):
            a[2 * i] = pos[i]
            a[2 * i + 1] = neg[i]

        # Fill the remaining negatives at the end of the array.
        index = len(neg) * 2
        for i in range(len(pos) - len(neg)):
            a[index] = neg[len(pos) + i]
            index += 1

    return a
            
    pass
