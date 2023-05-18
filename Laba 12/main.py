from tkinter import *
def first():

    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название рестика - {self.restaurant_name}")
            print(f"Тип кузины - {self.cuisine_type}")

        def open_restaurant(self):
            print("Рестик открыт")


    class IceCreamStand(Restaurant):
        def __init__(self, restaraunt_name, cuisine_type, location, time):
            super().__init__(restaraunt_name, cuisine_type)
            self.flavors = ["Ванильное", "Шоколадное", "Фисташковое"]
            self.type_ice = ["морженое на палочке", "мягкое мороженое", "Эскимо"]
            self.location = location
            self.time = time

        def flavorss(self):
            return self.flavors
        def loc(self):
            print(f"Описание локации - {self.location}")
        def worktime(self):
            print(f"Время работы - {self.time}")

        def new_flavor(self):
            answer = input("Хотите добавить новый сорт мороженого? ")
            if answer == "Да":
                while answer == "Да":
                    self.flavors.append(input("Введите сорт мороженого, которые вы хотите добавить: "))
                    answer = input("Хотите добавить ещё один сорт мороженого? ")
                print(f"Новое меню: {self.flavors}")
            answer = input("Хотите удалить сорт мороженого? ")
            if answer == "Да":
                while answer == "Да":
                    delete = input("Введите сорт мороженого, который вы хотите удалить: ")
                    if delete in self.flavors:
                        self.flavors.remove(delete)
                    else:
                        print("Такого мороженого нет")
                    answer = input("Хотите удалить ещё один сорт мороженого? ")
                print(f"Новое меню: {self.flavors}")
        def check_flavor(self):
            answer = input("Хотите проверить наличие мороженого? ")
            if answer == "Да":
                answer_flavor = input("Введите сорт мороженого, которые вы хотите найти: ")
                if answer_flavor in self.flavors:
                    print("Такое мороженое в наличии")
                else:
                    print("Такого мороженого нет в наличии")


        def choose_ice(self):
            a = input(f"Выберите вкус мороженого {self.flavors}: ")
            if a in self.flavors:
                b = input(f"Выберите тип мороженого {self.type_ice}: ")
                if b in self.type_ice:
                    print(f"Ваше мороженое - {a + ' ' + b}")
                else:
                    print("Такого типа нет")
            else:
                print("Такого вкуса нет")

        def open_window(self):
            window = Tk()
            window.title("Доступные вкусы: ")

            window.geometry("500x250")
            p = 1
            for i in self.flavors:
                l = Label(window, text=i, font=("Graphik", 20))
                l.grid(row=p)
                p += 1
            window.mainloop()
    new_rest = IceCreamStand(input("Напишите название ресторана с мороженым: "), input("Напишите тип кухни: "), input("Напишите описание локации ресторана: "), input("Напишите время работы ресторана:"))
    new_rest.describe_restaurant()
    print(new_rest.flavorss())
    new_rest.loc()
    new_rest.worktime()
    new_rest.new_flavor()
    new_rest.check_flavor()
    new_rest.choose_ice()
    new_rest.open_window()



first()