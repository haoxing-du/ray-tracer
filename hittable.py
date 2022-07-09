from nntplib import NNTPPermanentError


class HitRecord:
    def __init__(self):
        self.p = None
        self.normal = None
        self.t = 0.0

class Hittable:
    def __init__(r, t_min, t_max, rec)