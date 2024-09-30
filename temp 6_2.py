class  Figure: #решается при задании одной стороны
    sides_count = 0
    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = bool

    def get_color(self):
        return self.__color

    def  __is_valid_color(self, new_color):
        flag = True
        for i in new_color:
            if isinstance(i, (list, tuple)):
                new_color = [name for group in new_color for name in group]
            break
        for i in new_color:
            if i < 0 or i > 255:
                 flag = False
                 break
        return flag

    def set_color(self, *new_color):
        if self.__is_valid_color(new_color) == True:
            self.__color = [*new_color]
    def  __is_valid_sides(self, *new_sides):
        flag = True
        for i in new_sides:
            if isinstance(i, (list, tuple)):
                new_sides = [name for group in new_sides for name in group]
            break
        if len(new_sides) != self.sides_count:
            flag = False
        else:
            for i in new_sides:
                if isinstance(i, int)==False:
                    flag = False
                    break
        return flag

    def get_sides(self):
        return self.__sides
    def set_sides(self, *new_sides):
        for i in new_sides:
            if isinstance(i, (list, tuple)):
                new_sides = [name for group in new_sides for name in group]
            break
        if self.__is_valid_sides(new_sides) == True:
            if len(new_sides) == self.sides_count:
                 self.__sides = [*new_sides]
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
        self.__radius = self.__len__()/2/3.14

    def get_square(self):
           return self.__radius**2*3.14



class Triangle(Figure):
    sides_count = 3

    def __init__(self, new_color, new_sides):
        Figure.__init__(self)
        self.set_color(*new_color)
        self.__color = self.get_color()
        self.set_sides(new_sides)
        self.__sides = self.get_sides()

    def get_square(self):
        return sum(self.__sides)
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
    def get_volume(self):
        return self.__sides[0]**3


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
