class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()



r1 = Rectangle(10, 5)
r2 = Rectangle(7, 8)

print("Area of r1:", r1.area())
print("Area of r2:", r2.area())

print("Perimeter of r1:", r1.perimeter())
print("Perimeter of r2:", r2.perimeter())


if r1 > r2:
    print("Rectangle r1 is larger than r2")
elif r1 == r2:
    print("Both rectangles have equal area")
else:
    print("Rectangle r2 is larger than r1")
