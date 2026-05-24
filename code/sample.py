# Parent class
class Car:
    def __init__(c, opinion, body, model):
        c.opinion = opinion
        c.body = body
        c.model = model

    def drive(c):
        print(f"Lets take {c.model} which is {c.opinion} for a drive")

    def passenger(c):
        print(f"Its a {c.body}, its too small")


# Child class
class Electric(Car):
    def __init__(c, opinion, body, model, fuel_type):
        super().__init__(opinion, body, model)
        c.fuel_type = fuel_type

    def tesla(c):
        print(f"Its a {c.model} and its {c.opinion}")

    def reply(c):
        print(f"Why are you crazy? Its a {c.model}, so its trash")


# Parent object
my_car = Car("bad", "SUV", "Scarpio")

my_car.drive()
my_car.passenger()

print("--------")

# Child object
tesla_car = Electric("good", "sedan", "Tesla Model S", "Electric")

tesla_car.drive()       # inherited
tesla_car.passenger()   # inherited
tesla_car.tesla()
tesla_car.reply()