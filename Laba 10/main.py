# import json
# with open("123.json", encoding='utf-8') as json_file:
#     data = json.load(json_file)
#     print(data["products"])
#     for product in data["products"]:
#         print(f"Название: {product['name']} \nЦена: {product['price']} \nВес: {product['weight']} \n{'В наличии' if product['available'] else 'Не в наличии'}\n")
# answer = input("Хотите ввести новые данные? ")
# while answer == "Да":
#     data["products"].append({
#         "name": input("Введите название товара: "),
#         "price": int(input("Введите цену товара: ")),
#         "available": "true" if input("Введите, в наличии ли товар: ") == "Да" else "false",
#         "weight": int(input("Введите вес товара: "))
#     })
#     with open("123.json", "w", encoding='utf-8') as outfile:
#         json.dump(data, outfile, ensure_ascii=False)
#     answer = input("Данные записаны, хотите ещё что-нибудь добавить? ")
#
#
# data = {}
# word = []
# with open("en-ru.txt", encoding="utf-8") as file:
#     for line in file:
#         alpha = []
#         for i in range(len(line.split(" - ")[1].split(", "))):
#             alpha.append(line.split(" - ")[1].split("\n")[0].split(", ")[i])
#         data[line.split(" - ")[0]] = alpha
#     for i in data:
#         for j in data[i]:
#             word.append(j)
#     word = sorted(list(set(word)))

data = {}
with open("en-ru.txt", "r") as file:
    for line in file:
        en_w = line.split(" - ")[0].strip()
        ru_w = line.split(" - ")[1].strip().split(", ")
        for i in ru_w:
            i = i.strip()
            if i in data.keys():
                data[i] = data[i] + "," + en_w
            else:
                data[i] = en_w
with open("ru-en.txt", "w") as file:
    for i in sorted(data.keys()):
        file.writelines(f"{i} - {data[i]}\n")