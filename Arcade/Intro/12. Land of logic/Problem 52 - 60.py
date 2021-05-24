"""
Problem: Longest Word
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

[output] string

The longest word from text. It's guaranteed that there is a unique output.
"""
def longestWord(text):
    if text.isalpha():
        return text
    cmax = 0
    clen = 0
    ms = ""
    for i in range(len(text)):
        if text[i].isalpha():
            clen += 1
        else:
            if clen > cmax:
                cmax = clen
                ms = text[i - clen: i]
            clen = 0
        if i == len(text) - 1:
            if clen > cmax:
                cmax = clen
                ms = text[i - clen + 1: i + 1]
    return ms 
"""
Problem: Valid Time
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string time

A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

[output] boolean

true if the given representation is correct, false otherwise.
"""
def validTime(time):
    
    if not time.count(":") == 1:
        return False
    
    hour = range(24)
    mins = range(60)

    h, m = time.split(":")
    h = int(h)
    m = int(m)

    if h in hour and m in mins:
        return True
    
    return False
"""
Problem: Sum up numbers
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
0 ≤ inputString.length ≤ 105.

[output] integer
"""
def sumUpNumbers(inputString):
    if inputString.isnumeric():
        return int(inputString)
    cl = 0
    x = [0]
    for i in range(len(inputString)):
        if inputString[i].isnumeric():
            cl += 1
        else:
            if cl > 0:
                n = int(inputString[i - cl: i])
                x.append(n)
            cl = 0
        if i == len(inputString) - 1:
            if inputString[i].isnumeric():
                n = int(inputString[i - cl +1: i + 1])
                x.append(n)
    s=sum(x)
    return s
"""
Problem: Different Squares
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 9.

[output] integer

The number of different 2 × 2 squares in matrix.v
"""
def differentSquares(matrix):
    sq = []

    def get_Square(i, j):
        square = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j],matrix[i + 1][j + 1]]
        return square
    
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            square = get_Square(i, j)
            if square not in sq:
                sq.append(square)
    
    return len(sq)
"""
Problem: Digit Product
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

[output] integer
"""
def digitsProduct(p):
    if p == 0:
        return 10
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == p:
            return i
    return -1 
"""
Problem: File Naming
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string names

Guaranteed constraints:
5 ≤ names.length ≤ 1000,
1 ≤ names[i].length ≤ 15.

[output] array.string
"""
def fileNaming(names):
    n = set()
    for i in range(len(names)):
        if not names[:i].count(names[i]) == 0:
            ln = len(names[i])
            c = names[:i].count(names[i])
            names[i] += "(" + str(c) + ")"
            while names[i] in n:
                c += 1
                names[i] = names[i][:ln + 1] + str(c) + ")"
        n.add(names[i])
    return names
 """
 Problem: Message from Binary code
 You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

Example

For code = "010010000110010101101100011011000110111100100001", the output should be
messageFromBinaryCode(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string code

A string, the encrypted message consisting of characters '0' and '1'.

Guaranteed constraints:
0 < code.length < 800.

[output] string

The decrypted message.
 """
def messageFromBinaryCode(code):
    decode = ""
    for i in range(0, len(code), 8):
        n = int(code[i:i + 8], 2)
        decode += chr(n)
    return decode
"""
Problem: Spiral Numbers
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Matrix size, a positive integer.

Guaranteed constraints:
3 ≤ n ≤ 100.

[output] array.array.integer
"""
def spiralNumbers(n):

    output = []

    for i in range(n):
        ln = []
        for j in range(n):
            ln.append(0)
        output.append(ln)
    c = 1
    row = 0
    clm = 0
    for i in range(n):
        for j in range(n):
            if i == 0:
                output[row][clm] = c
                c += 1
                if j != n - 1:
                    clm += 1
            else:
                if clm == n - 1:
                    if row == n - 1:
                        clm -= 1
                    else:
                        row += 1
                elif clm == 0:
                    if output[row - 1][clm] == 0:
                        row -= 1
                    else:
                        clm += 1
                elif row == n - 1:
                    clm -= 1
                elif output[row][clm + 1] == 0 and output[row - 1][clm] != 0:
                    clm += 1
                elif output[row][clm + 1] != 0 and output[row + 1][clm] == 0:
                    row += 1
                elif output[row + 1][clm] != 0 and output[row][clm - 1] == 0:
                    clm -= 1
                elif output[row][clm - 1] != 0 and output[row - 1][clm] == 0:
                    row -= 1
                print(row, clm)
                output[row][clm] = c
                c += 1
    return output
"""
Problem: Sudoku
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
sudoku(grid) = true;

For
grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
sudoku(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
These examples are represented on the image below.



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer grid

A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

Guaranteed constraints:
grid.length = 9,
grid[i].length = 9,
1 ≤ grid[i][j] ≤ 9.

[output] boolean

true if the given grid represents a correct solution to Sudoku, false otherwise.
"""
from itertools import chain


def sudoku(grid):
    for i in grid:
        if len(i) != len(set(i)):
            return False
    for i in range(9):
        clm = []
        for j in range(9):
            clm.append(grid[j][i])
        if len(clm) != len(set(clm)):
            return False
    for i in range(0, 9, 3):
        box = []
        for j in range(i, i + 3):
            box.append(grid[j][i:i + 3])
        box = list(chain.from_iterable(box))
        if len(box) != len(set(box)):
            print(box)
            return False
    return True
