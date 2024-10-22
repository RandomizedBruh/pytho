productList = ["маска", "трава", "игла", "чтот", "геометрия", "учебник", "геометрия"]

print(productList)

productList.index("трава")

index = productList.index("трава")
print("поиск индекса ",index)

productList.append("алгебра")
print("новый массив после append ", productList)

productList.clear()

print("массив после clear ", productList)
count = productList.count("геометрия")
print("количество в массиве ", count)

productList.pop(3)
print("После pop удаления", productList)


productList.insert(3,"обж")
print("После insert", productList)

productList.sort(reverse=True)
print("Отсортированный список", productList)


productList.remove("геометрия")
print("После remove", productList)

extend = productList.extend(["ВиС", "география"])
print("Новый объединенный список", productList)
 
