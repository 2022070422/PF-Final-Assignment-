class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, dob, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Job Title:", self.job_title)
        print("Basic Salary:", self.basic_salary)
        print("Age:", self.age)
        print("Date of Birth:", self.dob)
        print("Passport Details:", self.passport_details)

