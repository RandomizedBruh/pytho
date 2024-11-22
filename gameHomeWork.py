import time
import random
# character
# - hp
# - hunger
# - armor
# - inventory
# - damage

name = "bandu"
hpPlayer = 20
hungerPlayer = 20
armorPlayer = 0 
damagePlayer = 1
inventory = {
    "wood":64,
    "terracot":2
}

# print("Остановка")
# time.sleep(5)
# print("Продолжение")

name = "zombie"
zombieHp = 20
damageZombie = 1.5
armorZombie = 1
inventory = {
    "железный шлем": 1,
    "железный меч": 1
}

name = "skeleton"
skeletonHp = 20
damageSkeleton = 1
armorSkeleton = 0
inventory = {
    "bool": 1
}



isGame = True
while isGame == True:
    dice = random.randint(1,9)



    if dice == 9:
        print("Опа,зомбачок")
        choose = input("Выберете, что сделать 1. Атаковать 2. Защититься 3. Убежать")
        if choose == "1":
            zombieHp = zombieHp - damagePlayer 
            hpPlayer = hpPlayer - damageZombie / 2
            print("Вы нанесли", damagePlayer, "урона")
            print("у противника осталось", zombieHp, "хп")
            time.sleep(1)
        elif choose == "2":
            hpPlayer = hpPlayer - damageZombie / 3
            print("Вы защитились! У вас осталось", hpPlayer, "здоровья")
            continue
        elif choose == "3":
            print("Вы убежали")
            continue
        hpPlayer = hpPlayer - damageZombie
        print("Зомби нанёс", damageZombie, "урона")
        time.sleep(1)
    if dice == 6:
        print("Опа,скелетик")
        choose = input("Выберете, что сделать 1. Атаковать 2. Защититься 3. Убежать")
        if choose == "1":
            skeletonHp = skeletonHp - damagePlayer
            print("Вы нанесли", damagePlayer, "урона")
            print("У противника осталось", skeletonHp, "хп")
            time.sleep(1)
        elif choose == "2":
            hpPlayer = hpPlayer - damageSkeleton / 2
            print("Вы защитились! У вас осталось", hpPlayer, "Здоровья")
            continue
        elif choose == "3":
            print("Вы убежали")
            continue
        hpPlayer = hpPlayer - damageSkeleton
        print("Скелет нанёс", damageSkeleton, "урона")
        time.sleep(1)
    if hpPlayer <= 0:
        print("Ты умер(")
        isGame = False
        break
    print("Текущее здоровье:", hpPlayer)
    
    time.sleep(0.5)

print("Игра завершена")

