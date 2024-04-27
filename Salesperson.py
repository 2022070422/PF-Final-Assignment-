from EmployeeManagement.Employee import Employee
class Salesperson(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, dob, passport_details, sales_targets):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, dob, passport_details)
        self.sales_targets = sales_targets

    def display_details(self):
        super().display_details()
        print("Sales Targets:", self.sales_targets)
