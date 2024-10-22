
products = []

choose = None

while choose != "0":
    choose = input("0 - выйти\n1 - добавить список\n2 - удалить из списка\n3 - показать список\n4 - очистить список ")
    if choose == "0":
        print("Программа завершена")
    elif choose == "1":
        print("Добавить в список")
        product = input("Введите продукт который вам нужен: ")
        products.append(product)    
    elif choose == "2":
        print("Удалить из списка")
        product = input("Введите продукт который хотите удалить: ")
        if product in products:
            products.remove(product)
        else:
            print("Такого тут нету")
    elif choose == "3":
        print("\nСписок продуктов")
        for i in range(0, len(products)):
            print(f"{i+1}. {products[i]}")
        print("\n")
    elif choose == "4":
        print("Очистить список")
        products.clear()
    else:
        print("Ошибка: введен неверный код")

