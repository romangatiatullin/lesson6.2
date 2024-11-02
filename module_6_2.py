class Vehicle:
    __COLOR_VARIANTS = ["красный", "синий", "зеленый", "черный", "белый", "серебристый"]
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def  set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Vengalbi', 'Mercedes CLS ', 1000, 'красный')
vehicle1.print_info()
vehicle1.set_color('желтый')
vehicle1.set_color('синий')
vehicle1.owner = 'Ahmedik'
vehicle1.print_info()