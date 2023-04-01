import math
y0 = 1
x = 0.5
theta = math.radians(80)
g = 9.81
v0 = 44

y = y0 + x*math.tan(theta) - (g*x**2) / (2*(v0*math.cos(theta))**2)

print(f"The height of the projectile is {y:.2f} meters.")
