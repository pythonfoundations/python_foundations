
class Building ():
    def __init__ (self, material, color, number ):
        self.material = material
        self.color = color
        self.number = number
        if self.number <=0:
            print(self.material, "out of stock")
        elif 0 < self.number < 100:
            print(material, "color = ", color, ", residue = ", number ,", Warehouse")
        else: print(material, "color = ", color, ", residue = ", number ,", Remote warehouse")

    def plus_minus(cl):
        counter = input("In case you want to add material input + and number in case you want to take away input - and"
                        " number")
        for i in counter:
            if " " == i:
                counter = counter.replace(" ", "")
        cl.number = cl.number + int(counter[0:])
        print(cl.material, "color = ", cl.color, ", residue = ", cl.number,", Remote warehouse")


class Market (Building):
    def __init__(self, material, color,  number = 0, price = 0):
        self.number = number
        self.price = price
        Building.__init__(self, material, color, number)


desk = Market ("Brown desk", "Brown", 10, 15000)
cartoon = Building ("cartoon", "brown", 1000)
Market.plus_minus(desk)

