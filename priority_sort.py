from math import log2

"""
Priority Sort is a non-comparative, linear sorting algorithm for integers only.
The algorithm sort the numbers by their bits starting from their
least significant bit (LSB) and going to their most significant bit (MSB).
It uses an array of indexes to simulate a linked list, allowing to make insertions
in constant time, so each layer of bits are sorted in linear time complexity.

The logic of this algorithm is close to LSD Radix Sort (base 2),
but using an array of indexes instead of buckets.

    Time complexity (worst case) : O(n*log2(k)) with n the size of the array and
    k the max number in the array.

    Space complexity : O(n) with n the size of the array.

This algorithm has no practical purposes right now as the built-in 'sorted'
function of Python written in C will always be more effective than anything else
programmed in Python.

But I'm looking to make an implementation of it in C.
In C, using pre-existing linked list structures as a parameter, this algorithm
would be extremely effective, as it would have a constant space complexity
AND a linear time complexity. Making it the perfect sorting algorithm under
the right conditions (integers only, and linked list structure).

Author : Maniacobra
"""
def priority_sort(arr, return_arr = False):
    """
    Sort an array of intergers in linear time complexity.

    arr : an array of integers
    return_arr : if this function must return a new sorted array (True)
    or override the existing array (False)
    """
    assert arr is not None
    nbits = 0
    first = 0
    iarr = [] # Array of indexes
    n = len(arr)
    check_signs = False
    # Prepare data
    if n == 0:
        if return_arr:
            return []
        return
    for i in range(n):
        # Indexes
        if i == n - 1:
            iarr.append(None)
        else:
            iarr.append(i + 1)
        # Data check
        if arr[i] != 0:
            v = arr[i]
            assert type(v) is int, "Not an integer : " + str(v)
            if v < 0:
                check_signs = True
                v = -v
            b = int(log2(v)) + 1
            if b > nbits:
                nbits = b
    # Sorting
    for weight in range(nbits + (1 if check_signs else 0)): # From LSB to MSB then maybe sign
        sep = None
        next = first
        prevsep = None
        prev = None
        # Put the zeros at left and ones at right in linear time :
        while next is not None:
            v = arr[next]
            if weight == nbits:
                # Sign
                b = 0 if v < 0 else 1
            else:
                # Bit at position
                b = ((-v if v < 0 else v) >> weight) & 1
                if v < 0:
                    b = -(b - 1)
            if b == 1:
                if sep is None:
                    # Define the boundary between the zeros and ones
                    prevsep = prev
                    sep = next
                prev = next
                next = iarr[next]
            elif sep is not None: # That means we encounter a 0 and there's a 1 behind
                nextnext = iarr[next]
                # Insertion :
                if prevsep is None:
                    # Must change the start index of the list
                    iarr[next] = first
                    first = iarr[prev]
                else:
                    iarr[next] = iarr[prevsep]
                    iarr[prevsep] = iarr[prev]
                iarr[prev] = nextnext
                prevsep = next
                # Finished insertion
                next = nextnext
            else:
                prev = next
                next = iarr[next]
    # Final sorted array
    sortedarr = []
    next = first
    while next is not None:
        sortedarr.append(arr[next])
        next = iarr[next]
    if return_arr:
        return sortedarr
    for i in range(n):
        arr[i] = sortedarr[i]