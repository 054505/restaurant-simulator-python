from restaurant import *

# inherit to reuse code
# override to fit this restaurant needs
class SpicyDish(Dish):
    def __init__(self):
        spicyness = 0

    def get_spicyness(self):
        return self.spicyness

    def set_spicyness(self, level):
        if type(level) == int or type(level) == float:
            self.spicyness = level
        else:
            raise Exception("spicyness must be a value")

class SpicyRestaurant(Restaurant):
    def add_new_dish(self, name, price, level):
        self.menu[name] = SpicyDish()
        self.menu[name].set_name(name)
        self.menu[name].set_price(price)
        self.menu[name].set_spicyness(level)

    def print_menu(self):
        if bool(self.menu) == True:
            keys = self.menu.keys()
            for key in keys:
                print(key + ": £" + (str(self.menu[key].get_price()) + ","), "Spicyness: " + str(self.menu[key].get_spicyness()))
        else:
            raise Exception("empty menu")


spicy = SpicyRestaurant()

# restaurant's get_name and set_name test
print("restaurant's get_name and set_name test")
spicy.set_name("A Spicy Restaurant")
print(spicy.get_name())
print()

# spicy.print_menu()
print("restaurant's menu test")
spicy.add_new_dish("Fried Chicken", 10, 0)
print("add_new_dish, Fried Chicken, 10, 0")
spicy.add_new_dish("Spicy Fried Chicken", 12.5, 3)
print("add_new_dish, Spicy Fried Chicken, 12.5, 3")
print()

# should print full menu and price
print("print restaurant's menu")
spicy.print_menu()
print()

# check revenue
print("revenue: " + str(spicy.get_revenue()))
print()

# order some food
print("order one Fried Chicken, then check revenue")
spicy.sale(1, "Fried Chicken")

# check revenue
print("revenue: " + str(spicy.get_revenue()))
print()

# order some food
print("order two Spicy Fried Chicken, then check revenue")
spicy.sale(2, "Spicy Fried Chicken")

# check revenue
print("revenue: " + str(spicy.get_revenue()))
print()

# zero employee exception
# spicy.list_employee()

# hire Amy
print("employee methods test")
print("hire Amy then list employees")
spicy.hire_employee("Amy", 20)
spicy.list_employee()
print()

# hire more
print("hire Brown, Charles, Dave, then list employees")
spicy.hire_employee("Brown", 20)
spicy.hire_employee("Charles", 20)
spicy.hire_employee("Dave", 20)

# list employees
spicy.list_employee()
print()

# retire Amy
print("retire Amy, then list employees")
spicy.retire_employee("Amy")

# list employee
print("list employees")
spicy.list_employee()