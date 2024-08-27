
class House():
    def __init__(self,nam,flrs):
        self.name = nam
        self.number_of_floors = flrs

    def go_to(self, nf):
        if nf > self.number_of_floors or nf < 1:
            print("Такого этажа не существует")
        else:
            for i in range(nf):
                print(i+1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)