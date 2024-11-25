from app.model import Rectangle
from app.view import RectangleView

class RectangleController:
    def __init__(self):
        self.rectangles = []

    def create_rectangle(self, width, height, color):
        rectangle = Rectangle(width, height, color)
        self.rectangles.append(rectangle)
        return rectangle

    def display_all_rectangles(self):
        for rect in self.rectangles:
            RectangleView.display_rectangle(rect)

if __name__ == "__main__":
    controller = RectangleController()
    print("Creating rectangles...")
    r1 = controller.create_rectangle(10, 20, 'red')
    r2 = controller.create_rectangle(30, 15, 'blue')
    controller.display_all_rectangles()
