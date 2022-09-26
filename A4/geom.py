import math

class Point (object):
    #constructor
    def __init__ (self, x =0, y=0):
        self.x, self.y = x, y

    
    def dist (self, other):
        return math.hypot(self.x - other.x, self.y - self.y)

    #toString method
    def __str__ (self):
        return '(' + str(self.x) + ", " + str(self.y) + ')'

    def __eq__ (self, other):
        return abs(self.x - other.x) < 0.00000001 and abs(self.y - other.y) < 0.00000001

def main():
    
    #create Point objects
    a = Point()
    b = Point(3, 4)
    c = Point(3, 4)
    print(a)
    print(b)
    print(c)

    print(a.dist(b))
    print(b.dist(a))

    if(b ==c):
        print("Point objects are equal")
    

main()
    