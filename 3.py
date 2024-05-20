class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг {self.restaurant_name} обновился до {self.rating}")

# Создаем экземпляр класса Restaurant с начальным рейтингом
restaurant1 = Restaurant("YamiYami", "любая", 4.2)

# Выводим информацию о ресторане до обновления рейтинга
restaurant1.describe_restaurant()

# Обновляем рейтинг ресторана
restaurant1.update_rating(4.9)
