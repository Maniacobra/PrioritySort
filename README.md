# PrioritySort

Priority Sort is a non-comparative, linear sorting algorithm for integers only.

The algorithm sort the numbers by their bits starting from their least significant bit (LSB) and going to their most significant bit (MSB).
It uses an array of indexes to simulate a linked list, allowing to make insertions in constant time, so each layer of bits are sorted in linear time complexity.

The logic of this algorithm is close to LSD Radix Sort (base 2), but using an array of indexes instead of buckets.

- Time complexity (worst case) : `O(n*log2(k))` with `n` the size of the array and `k` the max number in the array.
- Space complexity : `O(n)` with `n` the size of the array.

------

This algorithm has no practical purposes right now as the built-in 'sorted' function of Python written in C will always be more effective than anything else programmed in Python.

But I'm looking to make an implementation of it in C.
In C, using pre-existing linked list structures as a parameter, this algorithm would be extremely effective, as it would have a constant space complexity AND a linear time complexity. Making it the perfect sorting algorithm under the right conditions (integers only, and linked list structure).

I had the idea for this algorithm before knowing the existence of LSD Radix Sort.
