from random import randint
import time

class warrior ():
    def __init__(self, name: str, level: int):
        self.name = name
        self.__health =  100
        self.level = level
        if self.level <=0:
            print("level can't be less then zero, minimum level == 1")
            self.level = 1
        elif self.level > 1:
            c = self.level - 1
            d = 1 + (c / 10)
            self.__health = int(self.__health * d)

    def attack (self, name_1, name_2):
        i = randint (1,100)
        print("The die will decide who will attack first ")
        time.sleep(2)
        if i % 2 == 0:
            print("die decided that ",  name_1.name," will attack first ")
            self.attack_1(name_1, name_2)
            time.sleep(2)
        else:
            print("die decided that ", name_2.name, " will attack first ")
            self.attack_2(name_1, name_2)
            time.sleep(2)

    def attack_1 (self, name_1, name_2):
        if name_1.__health > 0:
            time.sleep(1)
            c = randint(2,10)
            name_2.__health = name_2.__health - c
            print(name_1.name," level ==", name_1.level, " attack ", name_2.name, "demage is ", c , "health", name_2.name,
                  " = ", name_2.__health)
        else: return print(name_2.name, " wins ")

        if name_2.__health > 0:
            time.sleep(1)
            c = randint (2,10)
            name_1.__health = name_1.__health -c
            print(name_2.name, " level ==", name_2.level, " attack ", name_1.name, "demage is ", c, "health", name_1.name,
                  " = ", name_1.__health)
        else: return print(name_1.name, " wins ")
        return self.attack_1(name_1, name_2)

    def attack_2 (self, name_1, name_2):
        if name_2.__health > 0:
            time.sleep(1)
            c = randint(2, 10)
            name_1.__health = name_1.__health - c
            print(name_2.name, " level ==", name_2.level, " attack ", name_1.name, "demage is ", c, "health",
                  name_1.name, " = ", name_1.__health)
        else:
            return print(name_1.name, " wins ")

        if name_1.__health > 0:
            time.sleep(1)
            c = randint(2, 10)
            name_2.__health = name_2.__health - c
            print(name_1.name, " level ==", name_1.level, " attack ", name_2.name, "demage is ", c, "health",
                  name_2.name, " = ", name_2.__health)
        else:
            return print(name_2.__name, " wins ")
        return self.attack_2 (name_1, name_2)

warrior_1 = warrior ("ololo_1", 10 )
warrior_2 = warrior ("ololo_2", 10)

warrior_1.attack(warrior_1, warrior_2)