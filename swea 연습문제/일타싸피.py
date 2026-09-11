import math
print(math.pi)
degree = 30
rad = math.radians(degree)
print(rad)
degree = math.degrees(rad)

print(f"{math.sin(rad):.1f}")
print(f"{math.cos(rad):.1f}")
print(f"{math.tan(rad):.1f}")

b = 4
c = 5


a = math.sqrt(c**2 - b**2)
print(a)

print(math.asin(a/c))
print(math.acos(a/b))
print(math.atan(c/b))