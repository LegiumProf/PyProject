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

    new_restaurant = Restaurant("У Кузины", "вкусная")
    print(new_restaurant.restaurant_name)
    print(new_restaurant.cuisine_type)
    print()

    new_restaurant.describe_restaurant()
    new_restaurant.open_restaurant()

    print()

    restaurant1 = Restaurant(input("Введите название ресторана"), "фаст фуд")
    restaurant2 = Restaurant("Хмели Сунели", "Грузинская")
    restaurant3 = Restaurant("Теремок", "Русская")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def third():
    from random import randint
    class restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = randint(1,5)
        def describe_restaurant(self):
            print(f"Название рестика - {self.restaurant_name}")
            print(f"Тип кузины - {self.cuisine_type}")
            print(f"Рейтинг рестика - {self.rating}")

        def new(self):
            new_rating = int(input("Введите новый рейтинг ресторана(от 1 до 5): "))
            while new_rating < 1 or new_rating > 5:
                print("Ошибка! Вы ввели неверный рейтинг")
                new_rating = int(input("Введите новый рейтинг ресторана(от 1 до 5): "))
            self.rating = new_rating
            print(f"Название рестика - {self.restaurant_name}")
            print(f"Тип кузины - {self.cuisine_type}")
            print(f"Рейтинг рестика - {self.rating}")
    new_restaurant = restaurant("Макдональдс", "Фаст Фуд")
    new_restaurant.describe_restaurant()
    new_restaurant.new()

first()