import time
import random
# character
# - hp
# - hunger
# - armor
# - inventory
# - damage

name = "bandu"
hp = 20
hunger = 20
armor = 0 
damage = 1
inventory = {
    "wood":64,
    "terracot":2
}

# print("Остановка")
# time.sleep(5)
# print("Продолжение")

zombieHp = 20
damageZombie = 1.5
armorZombie = 0
inventory = {
    "железный шлем": 1,
    "железный меч": 1
}

skeletonHp = 20
damageSkeleton = 1
armorSkeleton = 0
inventory = {
    "bool": 1
}



isGame = True
while isGame == True:
    dice = random.randint(1,6)



    if dice == 5:
        print("Опа,зомбачок")
        choose = input("Выберете, что сделать 1. Атаковать 2. Защититься 3. Убежать")
        if choose == "1":
            zombieHp = zombieHp - damage 

        elif choose == "2":
            hp = hp - damageZombie / 3
        elif choose == "3":
            print("Вы убежали")
            continue
        hp = hp - damageZombie
        print("Зомби нанёс", damageZombie, "урона")
        time.sleep(1)
    if dice == 3:
        print("Опа,скелетик")
        hp = hp - damageSkeleton
        print("Скелет нанёс", damageSkeleton, "урона")
        time.sleep(1)

    if hp <= 0:
        print("Ты умер(")
        isGame = False
        break
    print("Текущее здоровье:", hp)
    
    time.sleep(0.5)

print("Игра завершена")

