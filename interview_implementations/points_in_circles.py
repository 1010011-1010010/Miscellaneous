"""
Goal

On a Cartesian plane, given a point of coordinates (A, B) and N circles. Each circle is specified by its center coordinates (x, y) and its radius r.
Calculate how many circles contains the point (A, B).
Note: the point is counted if it is either inside or on the circle.

Input
Line 1 : A pair of integers A and B which is the coordinates of the point in question.
Line 2 : An integer N which is the number of circles.
N next lines : Three integers x, y, r where (x, y) are the coordinates of a circle center and r is the circle radius.

Output
Line 1 : A single integer which is the number of circles that contains point (A, B).
Constraints
0 ≤ N ≤ 1000
-10000 ≤ A, B, x, y ≤ 10000
0 < r ≤ 10000

Inputs:

    first:

        circles = ["298 -359 351",
        "-597 497 669",
        "-188 241 503",
        "193 601 904",
        "312 869 603",
        "-51 166 636",
        "-198 -739 607",
        "-321 858 735",
        "672 673 935",
        "-266 467 16",
        "-195 898 202",
        "-753 35 297",
        "768 -515 659",
        "-126 -156 376",
        "-791 -424 480",
        "221 -173 792",
        "-894 681 443",
        "383 34 251",
        "-933 -624 474",
        "-862 171 430"]
        a, b = 42, 24
        n = 20

    second:
        circles = ["2 5 1",
        "0 5 2",
        "4 5 2",
        "2 9 4",
        "2 0 5"]
        a, b = 2, 5
        n = 5
"""

# copied from above examples
circles = ["2 5 1",
        "0 5 2",
        "4 5 2",
        "2 9 4",
        "2 0 5"]
a, b = 2, 5
n = 5

count = 0
for i in range(n):
    x, y, r = [int(j) for j in circles[i].split()]
    if (((x-a)**2 + (y-b)**2)) ** 0.5 <= r:
        count+=1
print(count)
