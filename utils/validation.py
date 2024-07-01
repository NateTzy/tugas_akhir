# utils/validation.py

def validate_salary(salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
