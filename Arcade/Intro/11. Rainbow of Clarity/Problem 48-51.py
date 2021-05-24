"""
Problem: is Digit
Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
isDigit(symbol) = true;
For symbol = '-', the output should be
isDigit(symbol) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] char symbol

A character which is either a digit or not.

Guaranteed constraints:
Given symbol is from ASCII table.

[output] boolean

true if symbol is a digit, false otherwise.
"""
def isDigit(symbol):
    return symbol.isnumeric()
"""
Problem: Line Encoding
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

String consisting of lowercase English letters.

Guaranteed constraints:
4 ≤ s.length ≤ 15.

[output] string

Encoded version of s.
"""
def lineEncoding(s):
    out = ""
    counter = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            if counter > 1:
                out += (str(counter) + s[i - 1])
            else:
                out += (s[i - 1])
            counter = 1
    if s[len(s) - 1] == s[len(s) - 2]:
        out += (str(counter) + s[len(s) - 1])
    else:
        out += (s[len(s) - 1])
    return out
"""
Problem: Chess Knights
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



Example

For cell = "a1", the output should be
chessKnight(cell) = 2.



For cell = "c2", the output should be
chessKnight(cell) = 6.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string cell

String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

Guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.

[output] integer
"""
def chessKnight(cell):
    a = "abcdefgh"
    b = "12345678"
    board = set()
    for i in a:
        for j in b:
            board.add(i + j)
    
    x, y = cell[0], cell[1]

    x, y = ord(x), int(y)

    moves = [chr(x+2)+str(y+1),chr(x+1)+str(y+2),chr(x+2)+str(y-1),chr(x+1)+str(y-2),
            chr(x-1)+str(y+2),chr(x-2)+str(y+1),chr(x-2)+str(y-1),chr(x-1)+str(y-2)]
    
    print(moves)

    count = 0
    for i in moves:
        if i in board:
            count += 1

    return count
 """
 Problem: Delete Digit
 Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 106.

[output] integer
 """
def deleteDigit(n):
    num = str(n)
    highest = 0
    for digit in range(len(num)):
        output = num[:digit] + num[digit + 1:]
        if int(output) > int(highest):
            highest = output
    return int(highest)
