class Employee:
    def __init__(self):
        self.hour = 0
        self.name = ""
        self.wage = 0

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        if hour > 0:
            self.hour = hour
        else:
            raise Exception("hour worked must be a value greater than zero.")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_wage(self):
        return self.wage

    def set_wage(self, wage):
        if wage > 0:
            self.wage = wage
        else:
            raise Exception("wage must be value greater than zero.")
