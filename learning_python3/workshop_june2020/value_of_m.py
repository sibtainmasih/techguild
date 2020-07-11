"""
Module to get value of m for a given k

Usage:
    python3 value_of_m.py 12
"""

import sys


def get_m(k):
    """
    Finds value of m such that m*(m-1)/2 <= k

    Arguments:
        k: int
    
    Returns:
        m an int value such that m*(m-1)/2 <=k
    """
    m=0
    while (m*(m-1)/2)<=k:
        m+=1
    else:
        m-=1
    return m

if __name__ == '__main__':
    k = int(sys.argv[1])
    m = get_m(k)
    print(f"k={k} => m={m}")