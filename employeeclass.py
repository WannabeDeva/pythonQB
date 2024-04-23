class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self):
        # Dummy logic: Assume a fixed percentage increase in salary
        self.emp_salary *= 1.1  # Increase salary by 10%

    def emp_assign_department(self, department):
        self.emp_department = department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

# Example usage:
emp1 = Employee(101, "John Doe", 50000, "Engineering")
emp1.calculate_emp_salary()  # Increase salary
emp1.print_employee_details()
