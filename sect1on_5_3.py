
class House():
    def __init__(self,nam,flrs):
        self.name = nam
        self.number_of_floors = flrs

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
	if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        if isinstance(other,House):
            return self.number_of_floors != other.number_of_floors

    def __lt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other,House):
            return self.number_of_floors >= other.number_of_floors

    def __le__(self, other):
        if isinstance(other,House):
            return self.number_of_floors <= other.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __add__(self, inc):
        if isinstance(inc,int):
            self.number_of_floors += inc
        return self

    def __radd__(self, inc):
        if isinstance(inc,int):
            return self.__add__(inc)

    def __iadd__(self, inc):
        if isinstance(inc,int):
            return self.__add__(inc)




    def go_to(self, nf):
        if isinstance(nf,int):
            if nf > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(nf):
                print(i+1)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__