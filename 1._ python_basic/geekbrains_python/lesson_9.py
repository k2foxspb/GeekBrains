class Car:
    def __init__(self, make, model, year, *args):
        self.my_list = []
        for arg in args:
            self.my_list.append(arg)
        self.make = make
        self.model = model
        self.year = year

    def __del__(self):
        print(f"I am destructor {self.model}")

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def __add__(self, other):
        return self.year + other.year

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, index):
        return self.my_list[index]

    def __call__(self, newsparam):
        print(f'вызов класса как функции c аргументом {newsparam}')
        self.model = newsparam

    def __repr__(self):
        return f'__repr__ Car: {self.model}'

    @property
    def my_method(self):
        return self.year


a = Car('drive', 'subaru', 2020, 'черная', 'красная')
b = Car('drive', 'oka', 2000)
print(a.model)
print(a)
print(a)
print(a + b, a, b)
print(a[1])
a('москвич')
print(a.my_method)


class Auto:
    # конструктор класса Auto
    def __init__(self, year):
        # Инициализация свойств.
        self.year = year

    # создаем свойство года
    @property
    def year(self):
        return self.__year

    # сеттер для создания свойств
    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    @property
    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"

    def __del__(self):
        print(f'I am destructor {self.__year}')


x = Auto(2090)
print(x.get_auto_year)
