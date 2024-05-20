class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

# Создаем три экземпляра класса Restaurant
restaurant1 = Restaurant("YamiYami", "любая")
restaurant2 = Restaurant("Buddy", "европейская")
restaurant3 = Restaurant("SushiPalki", "японская")

# Вызываем метод describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
