from vec3 import (Vec3, Point3, Color)

class Ray:
    def __init__(self, origin=Point3(), direction=Vec3()):
        self.orig = origin
        self.dir = direction
    
    def at(self, t):
        return self.orig + t * self.dir