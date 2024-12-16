class Car:
    name = ""
    speed = ""
    color = ""
    durability = 0
    owner = ""
    # конструктор который вызывается при создании объека от класса(просто функция)
    def __init__(self, newName, newSpeed, newColor, newDurability, newOwner="нема владельца"):
        # self - указатель на конкретную машину
        self.name = newName
        self.speed = newSpeed
        self.color = newColor
        self.durability = newDurability
        self.owner = newOwner
    def print_info(self):
        print(f"Марка авто:  {self.name}\nЦвет: {self.color}\nСкорость: {self.speed}\nПрочность: {self.durability}\nВладелец: {self.owner}")
    def move(self):
        print(f"Авто {self.name} едет со скоростью {self.speed} км/ч")

car1 = Car("coolcar", 1000, "WHITE", 100, "guy")
car2 = Car("anothercoolcar", 700, "BLACK", 100, "anotherguy")
car3 = Car("anothertwocoolcar", 800, "YELLOW", 100)

# car1.move()

class Player:
    nameP = ""
    classP = ""
    hpP = 0
    endurance = 0
    mana = 0
    weapon = ""
    armor = None
    damage= 0
    def __init__(self, newNameP, newClassP, newHpP, newEnduranceP, newManaP, newWeaponP="нема оружия", newArmorP="нема брони"):
        self.namep = newNameP
        self.classp = newClassP
        self.hp = newHpP
        self.endurance = newEnduranceP
        self.mana = newManaP
        self.weapon = newWeaponP
        self.armor = newArmorP

    def print_infoP(self):
        print(f"Имя игрока: {self.namep}\nКласс: {self.classp}\nХп: {self.hp}\nВыносливость: {self.endurance}\nОружие: {self.weapon}\nБронь: {self.armor}")
    def say(self,text):
        print(f"Игрок {self.namep} говорит: '{text}'")

player1 = Player("Фордик", "какойточелизфнфмода", 100, 100, 50)
# player1.print_infoP()
player1.hp = 20
player1.print_infoP()

player1.say("блин...*cry*")


class Enemy:
    ename =""
    eclass = ""
    ehp=""
    emana=""
    eweapon=""
    edamage=""
    def __init__(self, newename,neweclass,newehp,newedamage,neweweapon="нема оружия"):
        self.ename =newename 
        self.eclass=neweclass
        self.ehp=newehp
        self.eweapon=neweweapon
        self.edamage=newedamage
        
    def info(self):
        print(f"Имя противника: {self.ename}\nКласс: {self.eclass}\nХп: {self.ehp}\nОружие: {self.eweapon}\nДамаг: {self.edamage}")


enemy1 = Enemy("матр4сс","тожегайсмода", 100, 10)
enemy1.info()

  


# ⁣yes     yes  yes yes yes
# yesyes  yes  yes     yes
# yes yes yes  yes     yes
# yes  yesyes  yes     yes
# yes     yes  yes yes yes
