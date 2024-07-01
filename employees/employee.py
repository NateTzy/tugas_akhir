# employees/employee.py

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        return f"Name: {self.name}, Salary: ${self.salary}"
