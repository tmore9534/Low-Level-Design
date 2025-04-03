# Component interface
class Graphic:
    def move(self, x, y):
        pass
    
    def draw(self):
        pass

# Leaf: Represents simple elements (e.g., a dot)
class Dot(Graphic):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"Drawing a dot at ({self.x}, {self.y})")

# Leaf: Represents a circle (inherits from Dot)
class Circle(Dot):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}")

# Composite: Can contain other graphics (including other composites)
class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)
    #IMP, Processing the object as if its only one
    def draw(self):
        for child in self.children:
            child.draw()
        print("Drawing bounding box")

# Client code
editor = CompoundGraphic()
editor.add(Dot(1, 2))
editor.add(Circle(5, 3, 10))

group = CompoundGraphic()
group.add(Dot(2, 3))
group.add(Circle(10, 8, 5))

editor.add(group)
editor.draw() #process as a whole, client doesn't need know the underlying object.
