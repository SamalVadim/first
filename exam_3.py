# 1 Реализовать Рекурсию. Возведение числа x в степень y
# ИЛИ

# def func(x,y):
#     if y == 1:
#         return x
#     else:
#         return x*func(x,y-1)
# x = int(input('Number'))
# y = int(input('Stepen'))
# print('Resalt = ', func(x,y))


# Определить функцию, которая будет дублировать нули в списке и вернуть в виде итеррируемого
# объекта-коллекции.
# Input:                         Output:
# func([0,0,0])            --> [0,0,0,0,0,0]
# func([1,2,100,0,3,4,5,0])--> [1,2,100,0,0,3,4,5,0,0]

# def func(z):
#     x = []
#     for i in z:
#         x.append(i)
#         if i == 0:
#             x.append(0)
#     return x
#
# a = [1,2,100,0,3,4,5,0]
# print(func(a))


# 2 Определить функцию, которая проверяет является ли строка, введенная пользователем, целым числом.
# Решение задачи сдать ссылкой на GitHub.

# def chek(x):
#     try:
#         if int(x):
#             return True
#     except ValueError:
#         return False
#
# print(chek('3.5'))

# ИЛИ
# Даны две строки. Определить функцию, которая будет находить индекс второго вхождения второй строки в первую.
# Если подстрока ' ' вывести None. Решение сдать ссылкой на GitHub.
# Input:                                 Output:
# func('marry', 'r')            --> 3
# func('merry christmas', 's')  --> 14
# func('happy new year', ' ')   --> None

# def func(z, x):
#     if x != " ":
#         print(z.index(x, (z.index(x)) + 1))
#     else:
#         print('None')
#
#
# func('happy new year', ' ')

# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».

# class IceCream:
#
#     def __init__(self, ingrdient = None):
#         self.ingrdient = ingrdient
#
#     def info_about_icecream(self):
#         if self.ingrdient != None:
#             print('Мороженное and', self.ingrdient)
#         else:
#             print('Обычное мороженое')
# i = IceCream()
# i.info_about_icecream()



# 4 Инкапсуляция. Определить класс Car, который будет содержать конструктор,
# в котором будет инициализироваться private переменная maxprice,
# а также методы изменения и вывода максимальной стоимости машины.

# class Car:
#
#     def __init__(self, maxprice):
#         self.__maxprice = maxprice
#
#     @property
#     def maxprice(self):
#         print('Cost of car is ', self.__maxprice)
#         return self.__maxprice
#
#     @maxprice.setter
#     def maxprice(self, discont):
#         if 0 < discont<1:
#             self.__maxprice -= discont*self.__maxprice
#             print('Discont is', discont, 'and maxprice is', self.__maxprice)
#             return self.__maxprice
#
# bmw = Car(1000)
# bmw.maxprice
# bmw.maxprice = 0.2
# bmw.maxprice




# 5 Создать класс Animal и определить в нем метод make_a_sound(). Метод должен вывоводить строку
# "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно.
# Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю".
# в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.
# (Cat: make_a_sound() -> '<...>', Dog: make_a_sound() -> '<...>')
# class Animal:
#     @classmethod
#     def make_a_sound(cls):
#         print("Издает звук")
#
# class Cat(Animal):
#     @classmethod
#     def scratch(cls):
#         print("Царапать мебель")
#
# class Dog(Animal):
#     @classmethod
#     def dig(cls):
#         print("Рыть землю")
# vas = Cat()
# vas.make_a_sound()
#
# bob = Dog()
# bob.make_a_sound()
