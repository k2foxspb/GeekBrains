class OfficeEquipment:
    equipment = {}

    def __init__(self, equipment_type, total):
        self.equipment_type = equipment_type
        self.total = total
        self.__setitem__(equipment_type, total)
        print(f'на склад поступила новая оргтехника {self.equipment}')

    def __setitem__(self, name_equipment, total):
        self.equipment.update({name_equipment: total})

    def __getitem__(self, name_equipment):
        return self.equipment[name_equipment]

    def __str__(self):
        return str(self.equipment)

    @property
    def can_trade(self):
        return f'возможно продать {self} шт'

    @classmethod
    def sell(cls, equipment, count_sell):
        sell = cls.equipment[equipment] - count_sell
        return f'количество проданного товара: {count_sell}, остаток на складе {sell}'


class Printer(OfficeEquipment):
    def __init__(self, total, cost):
        super().__init__(equipment_type=Printer.__name__, total=total)
        self.cost = cost
        self.price_for_all = cost * total

    def sell_item(self, equipment, count_sell):
        self.sell(equipment, count_sell)
        sell_count = self.cost * count_sell
        if self.__valid_total(equipment, count_sell):
            self.equipment[equipment] -= count_sell
            self.total = self.equipment[equipment]
            return print(f'было на складе на сумму- {self.price_for_all}$\n'
                         f'осталось на складе- {self.equipment[equipment]}шт\n'
                         f'продано на сумму- {sell_count}$')
        else:
            return print('на сладе нет "{0}" в количестве {1} шт'.format(Printer.__name__, count_sell))

    def __valid_total(self, equipment, count_sell):
        if self.equipment[equipment] - count_sell > 0:
            return True


z = Printer(100, 50)  # Поступление на склад
z.sell_item('Printer', 101)  # Попытка продать больше чем есть
z.sell_item('Printer', 8)  # Продажа
print(z['Printer'])  # получение количества по ключу
print(z)  # Возвращает метод строковое значение
print(z.can_trade)  # Метод класса как атрибут
