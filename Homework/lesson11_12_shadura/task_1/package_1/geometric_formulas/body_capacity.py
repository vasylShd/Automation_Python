def sphere_volume(r):
    return round((4 / 3) * 3.14 * (r ** 3), 2)

def cone_volume(h, r):
    return round((1 / 3) * 3.14 * (r ** 2) * h, 2)

def parallelepiped_volume(a, b, c):
    return a * b * c

def cylinder_volume(h, r):
    return round(3.14 * (r ** 2) * h, 2)

if __name__ == '__main__':
    def cube_volume(a):
        return a ** 3