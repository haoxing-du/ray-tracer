import sys
from numpy import (pi, inf)
from numpy.random import (uniform)
from vec3 import (Vec3, Point3, Color, dot, unit_vector)
from color import (write_color)
from ray import (Ray)
from hittable import (HitRecord, Hittable)
from hittable_list import (HittableList)
from sphere import (Sphere)
from camera import (Camera)

def hit_sphere(center, radius, r):
    oc = r.orig - center
    a = r.dir.length_squared()
    half_b = dot(oc, r.dir)
    c = oc.length_squared() - radius ** 2
    discriminant = half_b ** 2 - a * c
    if discriminant < 0:
        return -1
    return (-half_b - discriminant ** 0.5) / a

def ray_color(r, world):
    ''' linearly blends white and blue'''
    rec = HitRecord()
    if world.hit(r, 0, inf, rec):
        return 0.5 * (rec.normal + Color(1, 1, 1))
    unit_direction = unit_vector(r.dir)
    t = 0.5 * (unit_direction.y + 1)
    return (1-t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)

def main():
    # image
    aspect_ratio = 16/9
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 10

    # world
    world = HittableList()
    world.add(Sphere(Point3(0, 0, -1), 0.5))
    world.add(Sphere(Point3(0, -100.5, -1), 100))

    # camera
    cam = Camera()

    # render
    print("P3")
    print(str(image_width) + ' ' + str(image_height))
    print("255")

    for j in range(image_height-1, -1, -1):
        print(f"Scanlines remaining: {j}", file=sys.stderr)
        for i in range(image_width):
            pixel_color = Color(0, 0, 0)
            for s in range(samples_per_pixel):
                u = (i + uniform(0,1)) / (image_width - 1)
                v = (j + uniform(0,1)) / (image_height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world)
            write_color(pixel_color, samples_per_pixel)
    print("Done!", file=sys.stderr)

if __name__ == '__main__':
    main()