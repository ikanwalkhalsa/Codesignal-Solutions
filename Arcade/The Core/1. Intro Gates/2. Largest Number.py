"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 9.

[output] integer

The largest integer of length n.
"""

def largestNumber(n):
    num = "9"*n
    return int(num)
