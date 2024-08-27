
class House():
    def __init__(self,nam,flrs):
        self.name = nam
        self.number_of_floors = flrs

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def go_to(self, nf):
        if nf < 1 or nf > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(nf):
                print(i+1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(-1)
h2.go_to(0)
h1.go_to(5)
h2.go_to(10)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
