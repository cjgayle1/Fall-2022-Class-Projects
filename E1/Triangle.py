# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name:

# Student UT EID:

# Course Name: CS 313E

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

class Triangle (object):

    # constructor
    def __init__ (self, a = Point(0,0), b = Point(0,0), c = Point(0,0)):
        self.a, self.b, self.c = a, b, c
        self.sides = [self.a.dist(self.b), self.b.dist(self.c), self.c.dist(self.a)]
        self.sides.sort()


    # TODO: YOUR CODE HERE


    # print string representation of Triangle
    def __str__(self):
      return "Point1: (" + str(self.a.x) + ", " + str(self.a.y) + "), Point2: (" + str(self.b.x) + ", " + str(self.b.y) + "), Point3: (" + str(self.c.x) + ", " + str(self.c.y) + ")"
  # TODO: YOUR CODE HERE

    # check if the triangle is similar to another triangle
    def __eq__ (self, other):

      other_sides = [other.a.dist(other.b), other.b.dist(other.c), other.c.dist(other.a)]

      other_sides.sort()
      return (self.sides[0] / other_sides[0] == self.sides[1] / other_sides[1] and self.sides[1] / other_sides[1] == self.sides[2] / other_sides[2] and self.sides[2] / other_sides[2] == self.sides[0] / other_sides[0])

    # TODO YOUR CODE HERE

    # check if triangle is obtuse or not
    def is_obtuse(self):
      return (self.sides[0] * self.sides[0]) + (self.sides[1] * self.sides[1]) < (self.sides[2] * self.sides[2])

    # TODO: YOUR CODE HERE

    # check if triangle is scalene
    def is_scalene (self):
      
      tol = 1.0e-8
      return (abs(self.sides[0] - self.sides[1]) >= tol) and (abs(self.sides[1] - self.sides[2]) >= tol) and (abs(self.sides[2] - self.sides[0]) >= tol)

 
    # TODO YOUR CODE HERE


######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print('A', triangleA)
    print('B', triangleB)

    print('A obtuse', triangleA.is_obtuse())
    print('B obtuse', triangleB.is_obtuse())

    print('A scalene', triangleA.is_scalene())
    print('B scalene', triangleB.is_scalene())

    print('A equals b', triangleA == triangleB)

if __name__ == "__main__":
    main()
