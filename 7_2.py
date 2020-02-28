"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @property
    def total(self):
        return f'Итого на пошив {self.title} шт. будет затрачено: {self.title / 6.5 + 0.5 + 2 * self.title + 0.3 :.2f} м ткани'

    @abstractmethod
    def abstract(self):
        return 'Abstract'

class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто потребуется: {self.title / 6.5 + 0.5 :.2f} м ткани'

    def abstract(self):
        return 'Abstract 2'


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма потребуется: {2 * self.title + 0.3 :.2f} м ткани'

    def abstract(self):
        return 'Abstract 3'

coat = Coat(35)
costume = Costume(55)
print('\n', coat.consumption(),'\n',coat.total,'\n', coat.abstract())
print('\n', costume.consumption(), '\n', costume.total, '\n', costume.abstract())

