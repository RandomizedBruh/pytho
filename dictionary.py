dictionary = {
    "помидор":"фрукт",
    "арбуз":"ягода",
    "age":100
}
dictionary["помидор"] = "овощ"
print(dictionary["помидор"])

# dictionary.clear()
# print(dictionary)

dictionary.pop("age")
dictionary["новое поле"] = True
print(dictionary)
dictionary.popitem()
print(dictionary)
print("Список ключей", dictionary.keys())
print("Список значений", dictionary.values())



player = {
    "Имя": "Bandu",
    "Здоровье": 100,
    "Уровень": 1,
    "Мана": 100,
    "Сила": 15,
    "Защита": 1
}


for key in player:
    print(f"{key} : {player[key]}")



enemy = { 
    "Имя": "Steve",
    "Здоровье": 200,
    "Мана": 150,
    "Сила": 20,
    "Защита": 3
}
print("\n")

for key in enemy:
    print(f"{key} : {enemy[key]}")


import time
import random
while True:
    if player["Здоровье"] <= 0:
        print("гаме овер")
        break
    elif enemy["Здоровье"] <= 0:
        print("Так этого бота")
        break
    

rand = random.randint(1,6)
if rand == 1:
    print(f"{player['Имя']} промахнулся")
    time.sleep(2)
else :
    print(f'{player["Имя"]} наносит {enemy["Имя"]} {player["Сила"]} урона')
    enemy["Здоровье"] -= player["Сила"]

print("\n Очередь противника\n")
    
rand = random.randint(1,6)
if rand == 1:
    print(f"{enemy['Имя']} промахнулся")
    time.sleep(2)
else:
    print(f'{enemy["Имя"]} наносит {player["Имя"]} {enemy["Сила"]} урона')
    player["Здоровье"] -= enemy["Сила"]
    print("\nОчередь игрока\n")
    time.sleep(0.7)


# доделать программу так, чтобы наносимый урон зависел от защиты
#урон вычисляется по формуле урон-
    
