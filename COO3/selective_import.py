from graphics.rectangle import area as rect_area, perimeter as rect_peri
from graphics.circle import area as circle_area, perimeter as circle_peri
from graphics.threeDgraphics.cuboid import surface_area as cuboid_area,volume as cuboid_vol
from graphics.threeDgraphics.sphere import surface_area as sphere_area,volume as sphere_vol

print("Rectangle Area:",rect_area(10,5))
print("Rectangle Perimeter:",rect_peri(10,5))

print("Circle Area:",circle_area(7))
print("Circle Perimeter:",circle_peri(7))

print("Cuboid Surface Area:",cuboid_area(2,3,4))
print("Cuboid Volume:",cuboid_vol(2,3,4))

print("Sphere Surface Area:",sphere_area(3))
print("Sphere Volume:",sphere_vol(3))
