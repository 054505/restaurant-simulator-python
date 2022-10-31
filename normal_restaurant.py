from restaurant import *

normal = Restaurant()

# restaurant's get_name and set_name test
print("restaurant's get_name and set_name test")
normal.set_name("A normal Restaurant")
print(normal.get_name())
print()

# restaurant's menu test
# normal.print_menu()
print("restaurant's menu test")
normal.add_new_dish("Fried Chicken", 10)
print("add_new_dish, Fried Chicken, 10")
normal.add_new_dish("Duck Breast", 50)
print("add_new_dish, Duck Breast, 50")
normal.add_new_dish("Fried Fish", 12.5)
print("add_new_dish, Fried Fish, 12.5")
print()

# should print full menu and price
print("print restaurant's menu")
normal.print_menu()
print()

# remove Duck Breast from menu
print("remove Duck Breast from menu, then print menu again")
normal.remove_dish("Duck Breast")

# print menu
normal.print_menu()
print()

# check revenue
print("check revenue")
print("revenue: " + str(normal.get_revenue()))
print()

# order some food
print("order one Fried Chicken, then check revenue")
print("sale, Fried Chicken, 1")
normal.sale(1, "Fried Chicken")

# check revenue
print("revenue: " + str(normal.get_revenue()))
print()

# order some more food
print("order two Fried Chicken, then check revenue")
print("sale, Fried Chicken, 2")
normal.sale(2, "Fried Chicken")

# check revenue
print("revenue: " + str(normal.get_revenue()))
print()

# zero employee exception
# normal.list_employee()

# hire Amy
print("employee methods test")
print("hire Amy then list employees")
normal.hire_employee("Amy", 20)
normal.list_employee()
print()

# hire more
print("hire Brown, Charles, Dave, then list employees")
normal.hire_employee("Brown", 20)
normal.hire_employee("Charles", 20)
normal.hire_employee("Dave", 20)

# list employees
normal.list_employee()
print()

# retire Amy
print("retire Amy, then list employees")
normal.retire_employee("Amy")

# list employee
print("list employees")
normal.list_employee()