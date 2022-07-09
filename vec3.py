class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __getitem__(self, i):
        if i == 0: return self.x
        if i == 1: return self.y
        if i == 2: return self.z
        raise IndexError("Index out of range!")

    def __setitem__(self, i, c):
        if i == 0: self.x = c
        elif i == 1: self.y = c
        elif i == 2: self.z = c
        else: raise IndexError("Index out of range!")

    def __add__(self, v):
        return Vec3(self.x + v.x,
                    self.y + v.y,
                    self.z + v.z)

    def __sub__(self, v):
        return self + (-v)

    def __mul__(self, c):
        return Vec3(self.x * c, self.y * c, self.z * c)

    def __rmul__(self, c):
        return self * c

    def __truediv__(self, c):
        return self * (1/c)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def length(self):
        return self.length_squared() ** 0.5
    
    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.z}]"
    
# aliases for 3D point and color
Point3 = Vec3
Color = Vec3

# Vec3 utitlity functions
def dot(u, v):
    return u.x * v.x + u.y * v.y + u.z * v.z

def cross(u, v):
    return Vec3(u.y * v.z - u.z * v.y,
                u.z * v.x - u.x * v.z,
                u.x * v.y - u.y * v.x)

def unit_vector(v):
    return v / v.length()