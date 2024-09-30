class  Figure:
    sides_count = 0
    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = bool

    def get_color(self):
        return self.__color

    def  __is_valid_color(self, new_color):
        flag = True
        print('на входе', type(new_color), new_color)
        for i in new_color:
            if isinstance(i, (list, tuple)):
                new_color = [name for group in new_color for name in group]
                print('выпрямлен', type(new_color), new_color)
            break
        print('после break', type(new_color), new_color)
        for i in new_color:
            print('i=', type(i), i)
            if i < 0 or i > 255:
                 flag = False
                 print('после цикла флаг', flag)
                 break
        print('флаг в valid color=', flag)
        return flag

    def set_color(self, *new_color):
        if self.__is_valid_color(new_color) == True:
            self.__color = [*new_color]
        print(self.__color)

    def  __is_valid_sides(self, new_sides):
        flag = True
        print('на входе', type(new_sides), new_sides)
        for i in new_sides:
            if isinstance(i, (list, tuple)):
                new_sides = [name for group in new_sides for name in group]
                print('выпрямлен', type(new_sides), new_sides)
            break
        print('после break', type(new_sides), new_sides)
        # flag = True
        print('в is_valid: длина new_sides=', len(new_sides),'new_sides=', new_sides, 'sides_count=', self.sides_count)
        if len(new_sides) != self.sides_count:
            flag = False
            print('флаг после неравенства кол-ва сторон', flag)
        else:
            for i in new_sides:
                print('i=', i)
                if isinstance(i, int)==False:
                    flag = False
                    print('флаг после пров на целое', flag)
                    break
        print('флаг в valid sides=', flag)
        return flag

    def get_sides(self):
        print('в get sides __sides', self.__sides)
        return self.__sides

    def set_sides(self, *new_sides):
        print('в set: new_sides=', new_sides, 'sides_count=', self.sides_count)
        print('ответ', self.__is_valid_sides(new_sides))
        for i in new_sides:
            if isinstance(i, (list, tuple)):
                new_sides = [name for group in new_sides for name in group]
                print('выпрямлен в set sides', type(new_sides), new_sides)
            break
        if self.__is_valid_sides(new_sides) == True:
            print('в set sides в if new =', new_sides, 'длина=', len(new_sides))
            if len(new_sides) == self.sides_count:
                 # self.__sides = list(*new_sides)
                 self.__sides = new_sides
                 print('новое len sides=', len(new_sides), 'sides count=', self.sides_count)
                 print('после проверки кол-ва сторон новая sides=', self.__sides, '__sides=',self.__sides)
        pass
    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, new_color, new_sides):
        Figure.__init__(self)
        self.set_color(*new_color)
        self.__color = self.get_color()
        self.set_sides(new_sides)
        self.__sides = self.get_sides()
        print(self.__color)
        print(self.__sides)
        self.__radius = self.__len__()/2/3.14
        print('радиус', self.__radius)

    def get_square(self):
           return self.__radius**2*3.14

# circle1 = Circle((200, 200, 100), 10)
# print('цвет круга', circle1.get_color())
#
# print(circle1)
# circle1.set_color(55, 66, 77)
# print('площадь круга',circle1.get_square())
# print('длина круга', len(circle1))
# circle1.set_sides(15) # Изменится
# print('изменение длины сторон', circle1.get_sides())

# class Triangle(Figure):
#     sides_count = 3
#     def __init__(self):
#         Figure.__init__(self)
#
#     def get_square(self):
#         return sum(self.__sides)
#
class Cube(Figure):
    sides_count = 12
    def __init__(self, new_color, new_sides):
        Figure.__init__(self)
        self.set_color(*new_color)
        self.__color = self.get_color()
        new_sides = [new_sides]*12
        self.set_sides(new_sides)
        self.__sides = self.get_sides()
        print('кол-во сторон', self.__sides)
    def get_volume(self):
        print('в объёме __sides', self.__sides)
        return self.__sides[0]**3

# cube1 = Cube((222, 35, 130), 6)
# cube1.set_color(300, 70, 15) #Не изменится
# print(cube1.get_color())
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# print(cube1.get_volume())

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

#Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())