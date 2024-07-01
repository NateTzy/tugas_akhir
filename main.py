def validate_salary(salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
    return True

if __name__ == "__main__":
    try:
        salary_input = float(input("Enter the salary: "))
        if validate_salary(salary_input):
            print("Salary is valid.")
    except ValueError as e:
        print(e)
