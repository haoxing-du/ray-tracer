from vec3 import (Vec3, Point3)
from ray import (Ray)

class Camera:
    def __init__(self):
        self.aspect_ratio = 16/9
        self.viewpoint_height = 2
        self.viewpoint_width = self.aspect_ratio \
                               * self.viewpoint_height
        self.focal_length = 1
        self.origin = Point3(0, 0, 0)
        self.horizontal = Vec3(self.viewpoint_width, 0, 0)
        self.vertical = Vec3(0, self.viewpoint_height, 0)
        self.lower_left_corner = self.origin \
                                 - self.horizontal/2 \
                                 - self.vertical/2 \
                                 - Vec3(0, 0, self.focal_length)
    
    def get_ray(self, u, v):
        return Ray(self.origin, 
                   self.lower_left_corner + u * self.horizontal
                    + v * self.vertical - self.origin)