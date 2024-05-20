class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт")

# Создаем экземпляр класса Restaurant
newRestaurant = Restaurant("YamiYami", "любая")

# Выводим атрибуты по отдельности
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

# Вызываем методы
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()