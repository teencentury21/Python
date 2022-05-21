# Write the class Point as outlined in the instructions
import numpy as np

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x=x
        self.y=y
    def distance_to_origin(self):
        return np.sqrt(self.x*self.x+self.y*self.y)
    def reflect(self,axis):
        if(axis=="x"):
            self.y*=-1
        if(axis=="y"):
            self.x*=-1

pt = Point(x=3.0)
pt.reflect("x")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())