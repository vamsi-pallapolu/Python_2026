class Car:
    def __init__(self, brand, model, speed):
        self._brand = brand
        self._model = model
        self._speed = speed

    # getters
    def get_speed(self): 
        return self._speed
    
    def increaseSpeed(self, speed):
        self._speed += speed

    def decreaseSpeed(self, speed):
        self._speed = self._speed - speed if self._speed > speed else 0

    def displayStatus(self):
        print(f"{self._brand} is moving at {self._speed} KM/HR")


c1 = Car("Toyota", "Hilux", 10)
c1.displayStatus()
print(c1._speed)
c1.increaseSpeed(30)
c1.displayStatus()  
c1.decreaseSpeed(10)
c1.displayStatus()