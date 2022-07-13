from vec3 import (dot)

class HitRecord:
    def __init__(self):
        self.p = None
        self.normal = None
        self.t = 0.0
        self.front_face = False
    
    def set_face_normal(self, r, outward_normal):
        front_face = dot(r.dir, outward_normal) < 0
        self.normal = outward_normal if front_face else -outward_normal

class Hittable:
    def __init__(self, center=None, radius=0):
        self.center = center
        self.radius = radius