class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_salary=None):
        if raise_salary:
            self.salary += raise_salary
        else:
            self.salary += 5000
        return self.salary
