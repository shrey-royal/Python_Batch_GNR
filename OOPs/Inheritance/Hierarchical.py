class Shape:
    def __init__(self, color):
        self._color = color

    def display_color(self):
        return f"Color: {self._color}"
    
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
def main():
    c = Circle(5, "Red")
    r = Rectangle(4, 6, "Blue")

    print(c.display_color(), "Area: ", c.area())
    print(r.display_color(), "Area: ", r.area())

if __name__ == "__main__":
    main()