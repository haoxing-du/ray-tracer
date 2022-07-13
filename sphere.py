from hittable import (HitRecord, Hittable)
from vec3 import (dot)

class Sphere(Hittable):
    def __init__(self, cen=None, r=0):
        self.center = cen
        self.radius = r
    
    def hit(self, r, t_min, t_max, rec):
        oc = r.orig - self.center
        a = r.dir.length_squared()
        half_b = dot(oc, r.dir)
        c = oc.length_squared() - self.radius ** 2

        discriminant = half_b ** 2 - a * c
        if discriminant < 0: return False
        sqrtd = discriminant ** 0.5

        # find the nearest root that lies in the acceptable range
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False
            
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)

        return True