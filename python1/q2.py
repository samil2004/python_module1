class Vechile:
    def start_engine(self):
        print("engine is start")
        

class Car(Vechile):

    def play_music(self):
        print("music play")

class ElectricCar(Car):
    def charge_battery(self):
        print("charge tha battery")

v1=Vechile()
v1.start_engine()
print()

c1=Car()
c1.start_engine()
c1.play_music()
print()

e1=ElectricCar()
e1.start_engine()
e1.play_music()
e1.charge_battery()