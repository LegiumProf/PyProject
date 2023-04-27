def first():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                     "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                     "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(f"Ваш словарь: {countries_dict}")
    print(f"Столица Германии - {countries_dict['Германия']}")
    for i in sorted(countries_dict):
        print(i, "-", countries_dict[i])

def second():
    alp = {
        "авеинорст": 1,
        "дклмпу": 2,
        "бгёья": 3,
        "йы": 4,
        "жзхцч": 5,
        "шэю": 8,
        "фщъ": 10
    }
    word = input("Введите слово: ")
    s = 0
    for i in word:
        for j in alp:
            for k in j:
                if i == k:
                    s += alp[j]
    print(s)

def third():
    import random
    students = ["Петров", "Иванов", "Куликов", "Нудов", "Какунов"]
    languages = ["Английский", "Китайский", "Японский", "Русский", "Испанский", "Арабский", "Французкий", "Итальянский", "Португальский", "Неменцкий"]
    dict = {}
    for student in students:
        lan = []
        for i in range(random.randint(1, 4)):
            lan.append(random.choice(languages))
        dict[student] = sorted(list(set(lan)))
    print(dict)
    who_know_china = []
    for student in students:
        print(f"{student} знает {len(dict[student])} языка")
        if "Китайский" in dict[student]:
            who_know_china.append(student)
    if len(who_know_china) > 0:
        print(f"{who_know_china} знает китайский")
    else:
        print("Никто не знает китайский")


first(), second(), third()