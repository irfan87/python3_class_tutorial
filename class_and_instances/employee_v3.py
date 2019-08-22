# a simple employee class - OOP in Python 3
# using decorator

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
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

    # a function for apply raised 
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        firstname, lastname, pay = emp_string.split('-')
        return cls(firstname, lastname, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

employee_1 = Employee('irfan', 'shukri', 60000)
employee_2 = Employee('test', 'user', 70000)

emp_str_1 = 'John-Doe-20000'
emp_str_2 = 'Jane-Doe-30000'

new_employee_1 = Employee.from_string(emp_str_1)
new_employee_2 = Employee.from_string(emp_str_2)
# print(new_employee_1)

print(new_employee_1.fullname())
print(new_employee_1.user_email_address())
print(new_employee_1.pay)

print(new_employee_2.fullname())
print(new_employee_2.user_email_address())
print(new_employee_2.pay)

import datetime
my_date = datetime.date(2019, 8, 22)
print(Employee.is_workday(my_date))