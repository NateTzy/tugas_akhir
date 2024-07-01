# employees/hr.py

from .employee import Employee

class HR(Employee):
    def __init__(self, name, salary, benefits):
        super().__init__(name, salary)
        self.benefits = benefits

    def calculate_salary(self):
        total_salary = self.salary + self.benefits
        return total_salary

    def display(self):
        return f"HR: {super().display()}, Benefits: ${self.benefits}"
