# a simple employee class - OOP in Python 3

class Employee:
    # initialize employee data
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

        # create an email address with first_name and last_name variable
        self.email_address = first_name + "." + last_name + "@company.com"

    def fullname(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    def user_email_address(self):
        return f'{self.first_name}.{self.last_name}@company.com'

employee_1 = Employee('irfan', 'shukri', 60000)
employee_2 = Employee('test', 'user', 70000)

# print out from the method in the employee class
print(employee_1.fullname())
print(employee_1.user_email_address())

# print out straight from the class
print(Employee.fullname(employee_2))
print(Employee.user_email_address(employee_2))
