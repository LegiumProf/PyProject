# 1 прога
#
# password = input("Введите пароль: ")
# isUpper = False
# isLower = False
# isNumber = False
# isSpec = False
# isLen = False
# if len(password) > 7:
#     isLen = True
# if password.isupper() == False:
#     isUpper = True
# if password.islower() == False:
#     isLower = True
# if password.isnumeric() == False:
#     isNumber = True
# for i in "!@#$%^&?":
#     for j in password:
#         if i == j:
#             isSpec = True
# if isLen == False:
#     print("Пароль слишком короткий")
# elif (isUpper == True) and (isLower == True) and (isNumber == True) and (isSpec == True):
#     print("ОК")
# else:
#     print("Пароль слишком простой")

# 2 прога
# sit = int(input("Введите номер места в вагоне: "))
# if (sit >= 1) and (sit <= 36) and sit % 2 == 0:
#     print("Верхнее не боковое место")
# elif (sit >= 1) and (sit <= 36) and sit % 2 != 0:
#     print("Нижнее не боковое место")
# elif sit >=37 and sit <= 54 and sit % 2 == 0:
#     print("Вверхнее боковое место")
# elif sit >= 37 and sit <= 54 and sit % 2 != 0:
#     print("Нижнее боковое место")

#3 прога

# year = int(input("Введите год: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Год високосный")
# else:
#     print("Год не високосный")

# 4 прога

# first = input("Введите первый цвет: ")
# second = input("Введите второй цвет: ")
# if first == "Красный" or first == "Синий" or first == "Жёлтый":
#     if second == "Красный" or second == "Синий" or second == "Жёлтый":
#         if first == "Красный" and second == "Синий":
#             print("Фиолетовый")
#         if first == "Красный" and second == "Жёлтый":
#             print("Оранжевый")
#         if first == "Синий" and second == "Жёлтый":
#             print("Зелёный")
#
#     else:
#         print("Ошибка")
# else:
#     print("Ошибка")

# 5 прога

N = int(input("Введите, сколько слов вы хотите ввести: "))
string = ""
for i in range(0, N):
    string += input() + " "
print(string)
