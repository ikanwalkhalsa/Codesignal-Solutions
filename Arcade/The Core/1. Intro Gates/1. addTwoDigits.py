"""
Problem: addTwoDigits
Given
You are given a two-digit integer n. Return the sum of its digits.

Example

Example 1
For n = 29, the output should be addTwoDigits(n) = 11.

Example 2
For n = 48, the output should be addTwoDigits(n) = 12.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive two-digit integer.

Guaranteed constraints:
10 ≤ n ≤ 99.

[output] integer

The sum of the first and second digits of n.
"""


def addTwoDigits(n):
    num = str(n)
    return int(num[0])+int(num[1])
