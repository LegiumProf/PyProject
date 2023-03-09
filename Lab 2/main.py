import os, fileinput
let = "A"
dict = {}
a = []
with open('synonyms.txt') as f:
    lines = f.readline()
    for line in f:
        if line != "\n":
            dict[line.split(" - ")[0]] = line.split(" - ")[1].split("\n")[0]
    word = input("Введите слово: ")
    if word in dict.keys():
        if "; " in dict[word]:
            print(dict[word].split("; ")[0])
            answer = input("Вас устраивает синоним? ")
            if answer == "Нет":
                for i in range(1, len(dict[word].split("; "))):
                    if answer == "Нет":
                        print(dict[word].split("; ")[i])
                    answer = input("Вас устраивает синоним? ")
                if answer == "Нет":
                    synonym = input("Тогда напишите ваш синоним: ")
                    with open("synonyms.txt", "w") as file:
                        for key in dict.keys():
                            if key[0] != let:
                                file.write("\n")
                                let = key[0]
                            if key == word:
                                file.write(key + " - " + dict[key] + "; " + synonym + "\n")
                            else:
                                file.write(key + " - " + dict[key] + "\n")
    else:
        print("Такого слова нет в нашем словаре")

