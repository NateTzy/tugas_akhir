# employees/manager.py

from .employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.salary + self.bonus
        return total_salary

    def display(self):
        return f"Manager: {super().display()}, Bonus: ${self.bonus}"

