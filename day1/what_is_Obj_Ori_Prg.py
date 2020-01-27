class Car():
    def __init__(self, **kwargs):
        # Key word arguments are dictionary
        # # We can use get("Keyword", "default")
        self.doors = 4
        self.windows = 4
        self.wheels = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$200")
    
class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.open_roof = True

    def openning_roof:
        print("I can open my roof!")


porche = Convertible(color = "Red")
print(porche.color)