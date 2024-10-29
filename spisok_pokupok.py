


# создание массива (списка) для хранения продуктов
products = []

# переменная для выбора действий
choose = None

# пока мы не ввели 0, программа будет работать
while choose != "0":

    # показ действий,которые мы можем совершить
    choose = input("0 - выйти\n1 - добавить список\n2 - удалить из списка\n3 - показать список\n4 - очистить список ")
    if choose == "0":
        print("Программа завершена")

        #функция добавления
    elif choose == "1":
        print("Добавить в список")
        product = input("Введите продукт который вам нужен: ")
        products.append(product)

        # функция удаления хр 
    elif choose == "2":
        print("Удалить из списка")
        product = input("Введите продукт или его номер, который хотите удалить: ")
        if product in products:
            products.remove(product)

            # а тут для выбора номера
        elif product.isnumeric():
            num =  int(product)

            if num <= len(product):
                products.pop(num-1)
                print("удаляем элемент с номером", num)

                # это для разочарования пользователя который хотел выйти за предел списка
            else:
                print("Номер продукта выходит за границы  списка")

        else:
            print("Такого тут нету")

            # это показ списка
    elif choose == "3":
        print("\nСписок продуктов")
        for i in range(0, len(products)):
            print(f"{i+1}. {products[i]}")
        print("\n")


        # ну а это очистка списка
    elif choose == "4":
        print("Очистить список")
        products.clear()
    else:
        print("Ошибка: введен неверный код")

