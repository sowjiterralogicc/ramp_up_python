import math

class Shape:
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

def main():
    shape_choice = input("Choose a shape (square/triangle/circle): ").lower()

    if shape_choice == "square":
        side = float(input("Enter the side length of the square: "))
        shape = Square(side)
    elif shape_choice == "triangle":
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        shape = Triangle(base, height)
    elif shape_choice == "circle":
        radius = float(input("Enter the radius of the circle: "))
        shape = Circle(radius)
    else:
        print("Invalid shape choice")
        return

    area = shape.calculate_area()
    print(f"Area of {shape.__class__.__name__}: {area:.2f}")

if __name__ == "__main__":
    main()
