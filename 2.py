"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
   Основная сущность (класс) этого проекта — одежда,
   которая может иметь определенное название.
   К типам одежды в этом проекте относятся пальто и костюм.
   У этих типов одежды существуют параметры:
   размер (для пальто) и рост (для костюма).
   Это могут быть обычные числа: V и H, соответственно.
   Для определения расхода ткани по каждому типу одежды использовать формулы:
   для пальто (V/6.5 + 0.5),
   для костюма (2 * H + 0.3).
   Проверить работу этих методов на реальных данных.
   Реализовать общий подсчет расхода ткани.
   Проверить на практике полученные на этом уроке знания:
   реализовать абстрактные классы для основных классов проекта,
   проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def material_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v) -> None:
        self.V = v
    
    @property
    def material_consumption(self):
        return self.V / 6.5 + 0.5


class Suite(Clothes):
    def __init__(self, h) -> None:
        self.H = h
    
    @property
    def material_consumption(self):
        return 2 * self.H + 0.3
    

s_1 = Suite(180)
s_2 = Suite(200)

c_1 = Coat(180)
c_2 = Coat(200)

total_material_consumption = s_1.material_consumption + s_2.material_consumption + c_1.material_consumption + c_2.material_consumption
print(f"Общий расход ткани: {total_material_consumption}")