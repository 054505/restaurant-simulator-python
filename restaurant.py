from dish import *
from employee import *

class Restaurant:
    def __init__(self):
        self.address = ""
        self.menu = {}
        self.employees = {}
        self.name = ""
        self.revenue = 0

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def add_new_dish(self, name, price):
        self.menu[name] = Dish()
        self.menu[name].set_name(name)
        self.menu[name].set_price(price)

    def remove_dish(self, name):
        del self.menu[name]

    def print_menu(self):
        if bool(self.menu) == True:
            keys = self.menu.keys()
            for key in keys:
                print(key + ": £" + str(self.menu[key].get_price()))
        else:
            raise Exception("empty menu")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_revenue(self):
        return self.revenue

    def set_revenue(self, amount):
        if type(amount) == int or type(amount) == float:
            self.revenue += amount
        else:
            raise Exception("amount must be a value")

    def sale(self, quantity, name):
        if type(quantity) == int:
            amount = quantity * self.menu[name].get_price()
            self.set_revenue(amount)
        else:
            raise Exception("quantity must be an integer")

    def hire_employee(self, name, wage):
        self.employees[name] = Employee()
        self.employees[name].set_name(name)
        self.employees[name].set_wage(wage)

    def retire_employee(self, name):
        del self.employees[name]

    def list_employee(self):
        if bool(self.employees) == True:
            keys = self.employees.keys()
            for key in keys:
                print(key + ", Wage: £" + str(self.employees[key].get_wage()))
        else:
            raise Exception("zero employee")
