from hittable import (HitRecord, Hittable)

class HittableList(Hittable):
    def __init__(self, objects=[]):
        self.objects = objects

    def clear(self):
        self.objects = []
    
    def add(self, object):
        self.objects.append(object)

    def hit(self, r, t_min, t_max, rec):
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for object in self.objects:
            if object.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                # is there a better way to do this?
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.t = temp_rec.t
                rec.front_face = temp_rec.front_face
        
        return hit_anything