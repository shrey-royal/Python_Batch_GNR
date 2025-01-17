from abc import ABC, abstractmethod

# Abstract class
class FoodItem(ABC):    # ABC - abstract base class
    @abstractmethod
    def get_price(self):    # abstract method doesn't have any body
        pass

    @abstractmethod
    def get_description(self):
        pass

class Pizza(FoodItem):
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def get_price(self):
        base_price = 50
        topping_price = len(self.toppings) * 20
        if self.size == 'large':
            return base_price + topping_price + 150
        elif self.size == 'medium':
            return base_price + topping_price + 100
        else:
            return base_price + topping_price
        
    def get_description(self):
        return f"A {self.size} pizza with {', '.join(self.toppings)} toppings."
    
class Burger(FoodItem):
    def __init__(self, type_of_burger, extras):
        self.type_of_burger = type_of_burger
        self.extras = extras

    def get_price(self):
        base_price = 100
        extras_price = len(self.extras) * 20
        return base_price + extras_price

    def get_description(self):
        return f"A {self.type_of_burger} burger with {', '.join(self.extras)} extras."
    
class Salad(FoodItem):
    def __init__(self, type_of_salad, dressing):
        self.type_of_salad = type_of_salad
        self.dressing = dressing

    def get_price(self):
        base_price = 200
        return base_price

    def get_description(self):
        return f"A {self.type_of_salad} salad with {self.dressing} dressing."
    
def order_food(food_item: FoodItem):
    print(f"Description: {food_item.get_description()}")
    print(f"Total Price: Rs.{food_item.get_price()}")

def main():
    p = Pizza("large", ["Cheese", "Capsicum", "Tomato", "Olives"])
    b = Burger("cheeseburger", ['extra cheese', 'lettuce', 'tomato', 'onion'])
    s = Salad("Caeser", "ranch")

    order_food(p)
    order_food(b)
    order_food(s)

if __name__ == "__main__":
    main()
