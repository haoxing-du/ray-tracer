import sys
from vec3 import (Vec3, Point3, Color, dot, unit_vector)
from color import (write_color)
from ray import (Ray)

def hit_sphere(center, radius, r):
    oc = r.orig - center
    a = r.dir.length_squared()
    half_b = dot(oc, r.dir)
    c = oc.length_squared() - radius ** 2
    discriminant = half_b ** 2 - a * c
    if discriminant < 0:
        return -1
    return (-half_b - discriminant ** 0.5) / a

def ray_color(r):
    ''' linearly blends white and blue'''
    t = hit_sphere(Point3(0, 0, -1), 0.5 , r)
    if t > 0:
        N = unit_vector(r.at(t) - Vec3(0, 0, -1))
        return 0.5 * Color(N.x + 1, N.y + 1, N.z + 1)
    unit_direction = unit_vector(r.dir)
    t = 0.5 * (unit_direction.y + 1)
    return (1-t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)

def main():
    # image
    aspect_ratio = 16/9
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    # camera
    viewport_height = 2
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1

    origin = Point3(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 \
                        - vertical/2 - Vec3(0, 0, focal_length)

    # render
    print("P3")
    print(str(image_width) + ' ' + str(image_height))
    print("255")

    for j in range(image_height-1, -1, -1):
        print(f"Scanlines remaining: {j}", file=sys.stderr)
        for i in range(image_width):
            u = i / (image_width - 1)
            v = j / (image_height - 1)
            r = Ray(origin, lower_left_corner + u * horizontal 
                    + v * vertical - origin)
            pixel_color = ray_color(r)
            write_color(pixel_color)

    print("Done!", file=sys.stderr)

if __name__ == '__main__':
    main()