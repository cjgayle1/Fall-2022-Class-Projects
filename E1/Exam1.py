
import math

# point class used for triangle class
class Point(object):
    # initialization of Point object
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # handle print calling
    def __str__(self):
        return(f"({self.x}, {self.y})")

    # given another point, other, find the distance to it
    def dist(self, other):
        return(math.hypot(self.x - other.x, self.y - other.y))


    
