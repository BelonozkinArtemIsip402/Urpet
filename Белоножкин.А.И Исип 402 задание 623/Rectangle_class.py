class Rectangle:
    def __init__(self, width, height, id):
        self.id = id
        self.width = width
        self.height = height

    def perimeter(self):

        return 2 * (self.width + self.height)

    def area(self):
        
        return self.width * self.height
