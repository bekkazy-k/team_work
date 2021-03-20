class Car:
    def __init__(self, name, year, own_name):
        self.name = name
        self.year = year
        self.own_name = own_name

    def get_info(self):
        print(f'автомобиль {self.name}')
        print(f'год выпуска {self.year}')
        print(f'владелец {self.name}')

    