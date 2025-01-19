from colledtions import namedtuple
point = namedtuple("Point", ["x","y"])
p = point(1,2)
print(p.x)
print(p.y)
