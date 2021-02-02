class Car(object):
    def __init__(self, model, seats, color, brand):
        self.model = model
        self.seats = seats
        self.color = color
        self.brand = brand
    def getColor(self):
        print(self.color)
    def changeColor(self):
        colorChange = input("Change the colour of your car: ")
        self.color = colorChange

Honda = Car("Sedan",4,"grey","Honda")
Honda.getColor()
Honda.changeColor()
Honda.getColor()