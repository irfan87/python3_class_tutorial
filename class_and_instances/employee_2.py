# a simple employee class - OOP in Python 3

class Employee:
    # define the raise_amount and num_of_emps variable
    num_of_emps = 0
    raise_amount = 1.04

    # initialize employee data
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    def user_email_address(self):
        return f'{self.first_name}.{self.last_name}@company.com'

    # a function for apply raised 
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

employee_1 = Employee('irfan', 'shukri', 60000)
employee_2 = Employee('test', 'user', 70000)

# print out from the method in the employee class
print(employee_1.fullname())
print(employee_1.user_email_address())

# print out the raised that employee_1 should get
# print(employee_1.pay)
# employee_1.apply_raise()
# print(employee_1.pay)

# Employee.raise_amount = 1.05
employee_1.raise_amount = 1.05

print(employee_1.__dict__)
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

print(Employee.num_of_emps)
print(Employee.__dict__)