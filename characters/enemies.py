from characters.character import Character

class Bat(Character):
    def __init__(self,name = "Bat",hp=20,mp=0,atk=10,defense=3):
        super().__init__(name,hp,mp,atk,defense)

class Goblin(Character):
    def __init__(self,name="Goblin",hp=30,mp=10,atk=13,defense=4):
        super().__init__(name,hp,mp,atk,defense)

class Skeleton(Character):
    def __init__(self,name="Skeleton",hp=45,mp=0,atk=12,defense=0):
        super().__init__(name,hp,mp,atk,defense)

class DragonKing(Character):
    def __init__(self,name="Dragon King",hp=9999,mp=9999,atk=450,defense=450):
        super().__init__(name,hp,mp,atk,defense)
