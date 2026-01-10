class Car:
    def __init__(self, make, model, year):
        #initialise attributes
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        #return neatly formatted name
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name
    
    def read_odometer(self):
        #print a statement showing the cars mileage
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        #set the odometer reading to the given value
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the an odometer")

    def increment_odometer(self, miles):
        #add a given amount to the odometer reading
        self.odometer_reading += miles
            

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer

my_used_car.increment_odometer(100)
my_used_car.read_odometer


class ElectricCar(Car):
    def __init__(self, make, model, year):
        #initialised attributes from parent class
        super().__init__(make, model, year)
        #attribute specifc to a electric car
        self.battery_size = 40
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
