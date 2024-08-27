
class House():
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    
    def __init__(self,nam,flrs):
        self.name = nam
        self.number_of_floors = flrs

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstanse(other,House):
            return self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        if isinstanse(other,House):
            return self.number_of_floors != other.number_of_floors

    def __lt__(self, other):
        if isinstanse(other,House):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstanse(other,House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstanse(other,House):
            return self.number_of_floors >= other.number_of_floors

    def __le__(self, other):
        if isinstanse(other,House):
            return self.number_of_floors <= other.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __add__(self, inc):
        if isinstanse(inc,int):
            self.number_of_floors += inc
        return self

    def __radd__(self, inc):
        if isinstanse(inc,int):
            return self.__add__(inc)

    def __iadd__(self, inc):
        if isinstanse(inc,int):
            return self.__add__(inc)




    def go_to(self, nf):
        if nf < 1 or nf > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(nf):
                print(i+1)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del(h2)
del h3

print(House.houses_history)
