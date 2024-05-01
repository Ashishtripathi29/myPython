class Car:
    def __init__(self,id) -> None:
        print("new car blueprint created...")
        self.id=id
        self.name=None
    def printing(self):
        print(f"car id:{self.id}\ncar name:{self.name}")
    


my_car=Car("01")
my_car.name="maruti"
my_car.printing()
