# 抽象类需要继承abc.ABC
# 装饰器@abstractmethod定义抽象方法

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Woof!')

class Cat(Animal):
    def make_sound(self):
        print('miao')


class Dog2(Animal):
    def make_sound(self):
        pass

