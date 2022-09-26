#  File: Geometry.py

#  Description:
# Geometry has classes that each represent shapes or points
# these classes also have methods to compare one another to each other.
# Classes: Point, Sphere, Cube, Cylinder

#  Student Name: Christopher Gayle

#  Student UT EID: cjg4383

#  Partner Name: Kai Pang

#  Partner UT EID: ktp577

#  Course Name: CS 313E

#  Unique Number: 57535

#  Date Created: 9/12/22

#  Date Last Modified: 9/18/22

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x, self.y, self.z = x, y, z
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return("(" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(float(self.z)) + ")")

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6
    return (abs( (self.x + self.y + self.z) - (other.x + other.y+ other.z)) < tol)
class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x, self.y, self.z = x, y, z
    self.radius = radius
    self.center = Point(self.x, self.y, self.z)
  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return("Center: (" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(float(self.z)) + "), Radius: " + str(float(self.radius)))
  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return 4 * math.pi * self.radius * self.radius

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return 4 / 3 * math.pi * self.radius * self.radius * self.radius
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    # print(self.center)
    # print(p)
    # print(self.center.distance(p))
    # print(self.radius)
    return self.center.distance(p) < self.radius
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    return abs(self.radius - self.center.distance(Point(other.x, other.y, other.z))) >  other.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    # test each vertic with is inside point to test if the cube is in the sphere
      x, y, z, d = a_cube.x, a_cube.y, a_cube.z, a_cube.side / 2

      if not self.is_inside_point(Point(x + d, y + d, z + d)):
        return False
      if not self.is_inside_point(Point(x - d, y + d, z + d)):
        return False
      if not self.is_inside_point(Point(x + d, y - d, z + d)):
        return False
      if not self.is_inside_point(Point(x - d, y - d, z + d)):
        return False
      if not self.is_inside_point(Point(x + d, y - d, z - d)):
        return False
      if not self.is_inside_point(Point(x - d, y - d, z - d)):
        return False
      if not self.is_inside_point(Point(x + d, y + d, z - d)):
        return False
      if not self.is_inside_point(Point(x - d, y + d, z - d)):
        return False
      return True

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    #put the sphere in a tiny box and test if its inside
    x, y, z, h, r = a_cyl.x, a_cyl.y, a_cyl.z, a_cyl.height / 2, a_cyl.radius
    if not self.is_inside_point(Point(x + r, y + h, z + r)):
      return False
    if not self.is_inside_point(Point(x - r, y + h, z + r)):
      return False
    if not self.is_inside_point(Point(x + r, y - h, z + r)):
      return False
    if not self.is_inside_point(Point(x - r, y - h, z + r)):
      return False
    if not self.is_inside_point(Point(x + r, y + h, z - r)):
      return False
    if not self.is_inside_point(Point(x - r, y + h, z - r)):
      return False
    if not self.is_inside_point(Point(x + r, y - h, z - r)):
      return False
    if not self.is_inside_point(Point(x - r, y - h, z - r)):
      return False
    return True

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean

  def is_not_inside_sphere(self, other):
    return self.radius + other.radius < self.center.distance(Point(other.x, other.y, other.z))

  def is_not_inside_cube (self, a_cube):
    # test each vertice with is inside point to test if the cube is in the sphere
      x, y, z, d = a_cube.x, a_cube.y, a_cube.z, a_cube.side / 2

      if self.is_inside_point(Point(x + d, y + d, z + d)):
        return False
      if self.is_inside_point(Point(x - d, y + d, z + d)):
        return False
      if self.is_inside_point(Point(x + d, y - d, z + d)):
        return False
      if self.is_inside_point(Point(x - d, y - d, z + d)):
        return False
      if self.is_inside_point(Point(x + d, y - d, z - d)):
        return False
      if self.is_inside_point(Point(x - d, y - d, z - d)):
        return False
      if self.is_inside_point(Point(x + d, y + d, z - d)):
        return False
      if self.is_inside_point(Point(x - d, y + d, z - d)):
        return False
      return True

  def does_intersect_sphere (self, other):
    return not self.is_inside_sphere(other) and not self.is_not_inside_sphere(other)
   
    #strictly outside and strictly inside then you know if they are both false its true


  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    return (not self.is_inside_cube(a_cube)) and (not self.is_not_inside_cube(a_cube))

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    return Cube(self.center.x, self.center.y, self.center.z, self.radius / (math.sqrt(3) / 2))

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x, self.y, self.z, self.side = x, y, z, side
    self.Xmax = self.x + self.side / 2
    self.Xmin = self.x - self.side / 2
    self.Ymax = self.y + self.side / 2
    self.Ymin = self.y - self.side / 2
    self.Zmax = self.z + self.side / 2
    self.Zmin = self.z - self.side / 2
    self.center = Point(self.x, self.y, self.z)
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return("Center: (" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(float(self.z)) + "), Side: " + str(float(self.side)))

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return self.side * self.side * 6

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side * self.side * self.side

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    return p.x < self.Xmax and p.x > self.Xmin and p.y < self.Ymax and p.y > self.Ymin and p.z < self.Zmax and p.z > self.Zmin

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    #might be wrong
    return Point(self.x, self.y, self.z).distance(Point(a_sphere.x, a_sphere.y, a_sphere.z)) + a_sphere.radius < self.side / 2

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      x, y, z, d = other.x, other.y, other.z, other.side / 2

      # check each vertice
      if not self.is_inside_point(Point(x + d, y + d, z + d)):
        return False
      if not self.is_inside_point(Point(x - d, y + d, z + d)):
        return False
      if not self.is_inside_point(Point(x + d, y - d, z + d)):
        return False
      if not self.is_inside_point(Point(x - d, y - d, z + d)):
        return False
      if not self.is_inside_point(Point(x + d, y - d, z - d)):
        return False
      if not self.is_inside_point(Point(x - d, y - d, z - d)):
        return False
      if not self.is_inside_point(Point(x + d, y + d, z - d)):
        return False
      if not self.is_inside_point(Point(x - d, y + d, z - d)):
        return False
      return True

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    x, y, z, h, r = a_cyl.x, a_cyl.y, a_cyl.z, a_cyl.height / 2, a_cyl.radius

    # check each vertice
    if not self.is_inside_point(Point(x + r, y + h, z + r)):
      return False
    if not self.is_inside_point(Point(x - r, y + h, z + r)):
      return False
    if not self.is_inside_point(Point(x + r, y - h, z + r)):
      return False
    if not self.is_inside_point(Point(x - r, y - h, z + r)):
      return False
    if not self.is_inside_point(Point(x + r, y + h, z - r)):
      return False
    if not self.is_inside_point(Point(x - r, y + h, z - r)):
      return False
    if not self.is_inside_point(Point(x + r, y - h, z - r)):
      return False
    if not self.is_inside_point(Point(x - r, y - h, z - r)):
      return False
    return True

  def is_not_inside_cube (self, a_cube):
    # test each vertic with is inside point to test if the cube does not intersects another cube
      x, y, z, d = a_cube.x, a_cube.y, a_cube.z, a_cube.side / 2

      # check each vertice
      if self.is_inside_point(Point(x + d, y + d, z + d)):
        return False
      if self.is_inside_point(Point(x - d, y + d, z + d)):
        return False
      if self.is_inside_point(Point(x + d, y - d, z + d)):
        return False
      if self.is_inside_point(Point(x - d, y - d, z + d)):
        return False
      if self.is_inside_point(Point(x + d, y - d, z - d)):
        return False
      if self.is_inside_point(Point(x - d, y - d, z - d)):
        return False
      if self.is_inside_point(Point(x + d, y + d, z - d)):
        return False
      if self.is_inside_point(Point(x - d, y + d, z - d)):
        return False
      return True
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    return not self.is_inside_cube(other) and not self.is_not_inside_cube(other)

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    if(not self.does_intersect_cube(other)):
      return 0
    count = 0
    Points = []
    x, y, z, d = other.x, other.y, other.z, other.side / 2

    # check if its inside and update count
    if self.is_inside_point(Point(x + d, y + d, z + d)):
      count += 1
      Points.append(Point(x + d, y + d, z + d))
    if self.is_inside_point(Point(x - d, y + d, z + d)):
      count += 1
      Points.append(Point(x - d, y + d, z + d))
    if self.is_inside_point(Point(x + d, y - d, z + d)):
      count += 1
      Points.append(Point(x + d, y - d, z + d))
    if self.is_inside_point(Point(x - d, y - d, z + d)):
      count += 1
      Points.append(Point(x - d, y - d, z + d))
    if self.is_inside_point(Point(x + d, y - d, z - d)):
      count += 1
      Points.append(Point(x + d, y - d, z - d))
    if self.is_inside_point(Point(x - d, y - d, z - d)):
      count += 1
      Points.append(Point(x - d, y - d, z - d))
    if self.is_inside_point(Point(x + d, y + d, z - d)):
      count += 1
      Points.append(Point(x + d, y + d, z - d))
    if self.is_inside_point(Point(x - d, y + d, z - d)):
      count += 1
      Points.append(Point(x - d, y + d, z - d))

    # one vertice inside the cube
    if(count == 1):
      l = abs(Points[0].x - self.x + self.side / 2)
      h = abs(Points[0].y - self.y + self.side / 2)
      w = abs(Points[0].z - self.z + self.side / 2)
      return l * w * h
    
    # two vertices in the cube
    elif(count == 2):

      if(Points[0].x - Points[1].x == other.side):
        l = other.side
        h = abs(Points[0].y - self.y + self.side / 2)
        w = abs(Points[0].z - self.z + self.side / 2)
      
      if(Points[0].y - Points[1].y == other.side):
        l = abs(Points[0].x - self.x + self.side / 2)
        h = other.side
        w = abs(Points[0].z - self.z + self.side / 2)
  
      if(Points[0].z - Points[1].z == other.side):
        l = abs(Points[0].x - self.x + self.side / 2)
        h = abs(Points[0].y - self.y + self.side / 2)
        w = other.side
    
    # 4 vertices in the cube
    elif(count == 4):
      
      if(Points[0].x - Points[1].x == other.side and Points[0].y - Points[1].y == other.side):
        l = other.side
        h = other.side
        w = abs(Points[0].z - self.z + self.side / 2)

      if(Points[0].y - Points[1].y == other.side and Points[0].z - Points[1].z == other.side):
        l = abs(Points[0].x - self.x + self.side / 2)
        h = other.side
        w = other.side
      
      else:
        l = other.side
        h = abs(Points[0].x - self.x + self.side / 2)
        w = other.side
    return l * w * h
      


  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    return Sphere(self.x, self.y, self.z, self.side / 2)
class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis

  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.x, self.y, self.z, self.radius, self.height = x, y, z, radius, height
    self.center = Point(self.x, self.y, self.z)
    self.Xmax = self.x + self.radius
    self.Xmin = self.x - self.radius
    self.Ymax = self.y + self.height / 2
    self.Ymin = self.y - self.height / 2
    self.Zmax = self.z + self.radius
    self.Zmin = self.z - self.radius
    self.bottom = Point(x, y, z + (height / 2))
    self.top = Point(x, y, z - (height / 2))

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return("Center: (" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(float(self.z)) + "), Radius: " + str(float(self.radius)) + ", Height: " + str(float(self.height)))

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius * self.radius

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return math.pi * self.radius * self.radius * self.height
  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    
    # checks the position of each point to see if its outside the dimensions of the cylinder
    if p.x > self.x - self.radius and p.x < self.x + self.radius:
      if p.y > self.y - self.radius and p.y < self.radius + self.y:
        if p.z > self.z - self.height / 2 and p.z < self.z + self.height / 2:
          return True


    return False
    # return (self.Xmin < p.x < self.Xmax) and (self.Ymin < p.y < self.Ymax) and (self.Zmin < p.z < self.Zmax)
    # if not(self.z - self.bottom.z < p.z < self.z + self.top.z):
    #   return False
    # if not (math.sqrt((self.center.x - p.x) ** 2 + (self.center.y - p.y) ** 2) < self.radius):
    #   return False
    # return True

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    return a_sphere.x + a_sphere.radius < self.Xmax and a_sphere.x + a_sphere.radius > self.Xmin and a_sphere.y + a_sphere.radius < self.Ymax and a_sphere.y + a_sphere.radius > self.Ymin and a_sphere.z + a_sphere.radius < self.Zmax and a_sphere.z + a_sphere.radius > self.Zmin


  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      x, y, z, d = a_cube.x, a_cube.y, a_cube.z, a_cube.side / 2

      # checks each vertice of the cube
      if not self.is_inside_point(Point(x + d, y + d, z + d)):
        return False
      if not self.is_inside_point(Point(x - d, y + d, z + d)):
        return False
      if not self.is_inside_point(Point(x + d, y - d, z + d)):
        return False
      if not self.is_inside_point(Point(x - d, y - d, z + d)):
        return False
      if not self.is_inside_point(Point(x + d, y - d, z - d)):
        return False
      if not self.is_inside_point(Point(x - d, y - d, z - d)):
        return False
      if not self.is_inside_point(Point(x + d, y + d, z - d)):
        return False
      if not self.is_inside_point(Point(x - d, y + d, z - d)):
        return False
      return True


  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    # x, y, z, h, r = other.x, other.y, other.z, other.height / 2, other.radius
    # if not self.is_inside_point(Point(x + r, y + h, z + r)):
    #   return False
    # if not self.is_inside_point(Point(x - r, y + h, z + r)):
    #   return False
    # if not self.is_inside_point(Point(x + r, y - h, z + r)):
    #   return False
    # if not self.is_inside_point(Point(x - r, y - h, z + r)):
    #   return False
    # if not self.is_inside_point(Point(x + r, y + h, z - r)):
    #   return False
    # if not self.is_inside_point(Point(x - r, y + h, z - r)):
    #   return False
    # if not self.is_inside_point(Point(x + r, y - h, z - r)):
    #   return False
    # if not self.is_inside_point(Point(x - r, y - h, z - r)):
    #   return False
    # return True
    # if x - r > self.x - self.radius and x + r < self.x + self.radius:
    #   if y - r > self.y - self.radius and y + r < self.y + self.radius:
    #     if z - h > self.z - self.height / 2 and z - h + self.height / 2:
    #       return True

    # return False
    # temp_cyl_center = Point(self.x, self.y, self.z)
    # if temp_cyl_center.y + self.radius < 
    # return self.radius > other.radius + Point(self.x,self.y,self.z).distance(Point(other.x, other.y, other.z)) and self.height > other.height
    
    # checks the edge of each position to see if it is touching
    r = self.radius
    h = self.height
    if other.x - other.radius > self.x - r and other.x + other.radius < self.x + r:
        if other.y - other.radius > self.y - r and other.y + other.radius < self.y + r:
            if other.z - other.height / 2 > self.z - h / 2 and other.z + other.height / 2 < self.z + h / 2:
                return True
    return False



    # d = self.center.distance(other.center)
    # return (self.radius > (other.radius + d))

    # d = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    # # Get maxes in min for self.cyl and other.cyl
    # Zmax = self.center.z + self.height
    # Zmin = self.center.z - self.height
    # ZmaxO = other.center.z + other.height
    # ZminO = other.center.z - other.height

    # return (d + other.r < self.r) and (Zmin < ZmaxO < Zmax) and (Zmin < ZminO < Zmax)


  def is_not_inside_cyl(self, other):
    # x, y, z, h, r = other.x, other.y, other.z, other.height / 2, other.radius
    # if self.is_inside_point(Point(x + r, y + h, z + h)):
    #   return False
    # if self.is_inside_point(Point(x - r, y + h, z + h)):
    #   return False
    # if self.is_inside_point(Point(x + r, y - h, z + h)):
    #   return False
    # if self.is_inside_point(Point(x - r, y - h, z + h)):
    #   return False
    # if self.is_inside_point(Point(x + r, y + h, z - h)):
    #   return False
    # if self.is_inside_point(Point(x - r, y + h, z - h)):
    #   return False
    # if self.is_inside_point(Point(x + r, y - h, z - h)):
    #   return False
    # if self.is_inside_point(Point(x - r, y - h, z - h)):
    #   return False
    # return True


        # if self.z > other.z:
        #     if other.z + other.height / 2 <= self.z - self.height / 2:
        #         return False
        # else:
        #     if self.z + self.height / 2 <= other.z - other.height / 2:
        #         return False
        # center_dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        # if center_dist < self.radius + other.radius:
        #     return True


    # checks the edge of each position to see if it is touching
    r = self.radius
    h = self.height
    if other.x + other.radius < self.x - r and other.x - other.radius > self.x + r:
        if other.y + other.radius < self.y - r and other.y - other.radius > self.y + r:
            if other.z + other.height / 2 < self.z - h / 2 and other.z - other.height / 2 > self.z + h / 2:
                return True
    return False

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    return not self.is_inside_cylinder(other) and not self.is_not_inside_cyl(other)
      
      
      # d = self.center.distance(other.center)
      # return (d < (self.radius + other.radius)) and (d < (self.height + other.height))
    

def main():
  # read data from standard input
  # read the coordinates of the first Point p
  Pcor = list(map(float, sys.stdin.readline().strip().split()[:3]))

  # create a Point object 
  q = Point(Pcor[0], Pcor[1], Pcor[2])
  # read the coordinates of the second Point q
  Qcor = list(map(float, sys.stdin.readline().strip().split()[:3]))

  # create a Point object 
  p = Point(Qcor[0], Qcor[1], Qcor[2])
  
  # read the coordinates of the center and radius of sphereA
  Acor = list(map(float, sys.stdin.readline().strip().split()[:4]))
  # create a Sphere object 
  sphereA = Sphere(Acor[0], Acor[1], Acor[2], Acor[3])
  # read the coordinates of the center and radius of sphereB
  Bcor = list(map(float, sys.stdin.readline().strip().split()[:4]))
 
  # create a Sphere object
  sphereB = Sphere(Bcor[0], Bcor[1], Bcor[2], Bcor[3])
  # read the coordinates of the center and side of cubeA
  Acor = list(map(float, sys.stdin.readline().strip().split()[:4]))
  # create a Cube object 
  cubeA = Cube(Acor[0], Acor[1], Acor[2], Acor[3])
  # read the coordinates of the center and side of cubeB
  Bcor = list(map(float, sys.stdin.readline().strip().split()[:4]))
  # create a Cube object 
  cubeB = Cube(Bcor[0], Bcor[1], Bcor[2], Bcor[3])
  # read the coordinates of the center, radius and height of cylA
  Acor = list(map(float, sys.stdin.readline().strip().split()[:5]))
  # create a Cylinder object 
  cylA = Cylinder(Acor[0], Acor[1], Acor[2], Acor[3], Acor[4])
  # read the coordinates of the center, radius and height of cylB
  Bcor = list(map(float, sys.stdin.readline().strip().split()[:5]))
  # create a Cylinder object
  cylB = Cylinder(Bcor[0], Bcor[1], Bcor[2], Bcor[3], Bcor[4])
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin

  TF = {True: "is", False: "is not"}
  DN = {True: "does", False: "does not"}
  print("Distance of Point p from the origin " + str(TF[p.distance(Point()) > q.distance(Point())]) + " greater than the distance of Point q from the origin")
  # print if Point p is inside sphereA
  print("Point p " + TF[sphereA.is_inside_point(p)] + " inside sphereA")
  # print if sphereB is inside sphereA
  print("sphereB " + str(TF[sphereA.is_inside_sphere(sphereB)]) + " inside sphereA")

  # print if cubeA is inside sphereA
  print("cubeA " + str(TF[sphereA.is_inside_cube(cubeA)]) + " inside sphereA")

  # print if cylA is inside sphereA
  print("cylA " + str(TF[sphereA.is_inside_cyl(cylA)]) + " inside sphereA")

  # print if sphereA intersects with sphereB
  print("sphereA " + DN[sphereB.does_intersect_sphere(sphereA)] + " intersect sphereB")
  # print if cubeB intersects with sphereB
  print("cubeB "+ DN[sphereB.does_intersect_cube(cubeA)] +" intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  print("Volume of the largest Cube that is circumscribed by sphereA " + TF[sphereA.circumscribe_cube().volume() >cylA.volume()] +" greater than the volume of cylA")
  # print if Point p is inside cubeA

  print("Point p " + TF[cubeA.is_inside_point(p)] + " inside cubeA")

  # print if sphereA is inside cubeA
  print("sphereA " + TF[cubeA.is_inside_sphere(sphereA)] + " inside cubeA")
  # print if cubeB is inside cubeA
  print("cubeB " + TF[cubeA.is_inside_cube(cubeB)] + " inside cubeA")

  # print if cylA is inside cubeA
  print("cylA " + TF[cubeA.is_inside_cylinder(cylA)] + " inside cubeA")

  # print if cubeA intersects with cubeB
  print("cubeA " + DN[cubeB.does_intersect_cube(cubeA)] + " intersect cubeB")

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  print("Intersection volume of cubeA and cubeB " + TF[cubeA.intersection_volume(cubeB) > sphereA.volume()] + " greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  print("Surface area of the largest Sphere object inscribed by cubeA " + TF[cubeA.inscribe_sphere().area() > cylA.area()] +" greater than the surface area of cylA")
 
  # print if Point p is inside cylA
  print("Point p " + TF[cylA.is_inside_point(p)] + " inside cylA")
  # print if sphereA is inside cylA
  print("sphereA " + TF[cylA.is_inside_sphere(sphereA)] +" inside cylA")

  # print if cubeA is inside cylA
  print("cubeA " + TF[cylA.is_inside_cube(cubeA)] +" inside cylA")

  # print if cylB is inside cylA
  print("cylB " + TF[cylA.is_inside_cylinder(cylB)] + " inside cylA")

  # print if cylB intersects with cylA
  print("cylB " + DN[cylA.does_intersect_cylinder(cylB)] + " intersect cylA")
if __name__ == "__main__":
  main()