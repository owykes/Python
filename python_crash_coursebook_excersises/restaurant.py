class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")


mcdonalds = Restaurant('mcdonalds','fast food')
pizza_express = Restaurant('pizza express', 'italian')
blakes = Restaurant('blakes', 'bistro')

print(mcdonalds.cuisine_type)
print(mcdonalds.restaurant_name)

mcdonalds.open_restaurant()
mcdonalds.describe_restaurant()
pizza_express.describe_restaurant()
blakes.describe_restaurant()
