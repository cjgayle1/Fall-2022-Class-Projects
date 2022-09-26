# File: Pattern.py

# Description: Given a sequence of number, find length traveled on number pad

# Student Name: 

# Student UT EID: 

# Course Name:

# Unique Number:

import sys
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)
        
  def __str__(self):
    return(f"({self.x}, {self.y})")

# Input: a list of integers representing the sequence of numbers traveled, len(ptrn) >= 2
# Output: distance traveled on the number pad
def unlock_pattern(ptrn):
    """TODO"""
    keypad = dict()
    keypad[1] = Point(0, 3)
    keypad[2] = Point(1, 3)
    keypad[3] = Point(2, 3)
    keypad[4] = Point(3, 3)
    keypad[5] = Point(0, 2)
    keypad[6] = Point(1, 2)
    keypad[7] = Point(2, 2)
    keypad[8] = Point(3, 2)
    keypad[9] = Point(0, 1)
    keypad[10] = Point(1, 1)
    keypad[11] = Point(2, 1)
    keypad[12] = Point(3, 1)
    keypad[13] = Point(0, 0)
    keypad[14] = Point(1, 0)
    keypad[15] = Point(2, 0)
    keypad[16] = Point(3, 0)

    dist = 0
    for i in range(len(ptrn) - 1):
        dist += keypad[ptrn[i]].dist(keypad[ptrn[i + 1]])
    return dist

# TAKE CAUTION TO EDIT BELOW THIS LINE
def main():
    line = sys.stdin.readline().split()
    input_pattern = []
    for ele in line:
        input_pattern.append(int(ele))
    print("{:.2f}".format(unlock_pattern(input_pattern)))

if __name__ == "__main__":
    main()