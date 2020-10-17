#Employee.py - A simple program that logs information about Employees and includes inheritance of Class Employee by subclasses Developer, Manager
class Employee:
    #class variables
    num_of_emps=0
    raise_amount= 1.04


    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay = pay
        self.email=first + '.' + last + '@gmail.com'
        
        Employee.num_of_emps += 1


    def fullname(self): 
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

 
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount= amount


    @classmethod 
    def from_string(cls, emp_str):
       first, last, pay = emp_str.split('-')
       return cls(first, last, pay)


#object instantiation
emp_1= Employee('Neema', 'Muganga', 100000)
emp_2= Employee('Test', 'User', 200000)

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Doey-80000'
emp_str3 = 'Jack-Den-90000' 

new_emp_1 =  Employee.from_string(emp_str1)

print(new_emp_1.email)
print(new_emp_1.pay)

Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


class Developer(Employee):
    raise_amount= 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees= employees

#Method that adds new employee information into the list
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

#A method that avoids duplicate employee logging by removing already existing employee information
    def remove_emp(self, emp):
       if emp in self.employees:
            self.employees.remove(emp)

#Method displays Employee information by their fullnames
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

#instantiating Subclass Developer's objects           
dev1 = Developer('Neema', 'Muganga', 100000, 'Python')
dev2 = Developer('Test', 'User', 200000, 'Java')
mgr1=Manager('Muganga', 'Neema', 300000, [dev2])

print(mgr1.email)
mgr1.add_emp(dev1)
mgr1.remove_emp(dev2)
mgr1.print_emps()

print(dev1.email)
print(dev2.prog_lang)

dev1.apply_raise()
print(help(Developer))# Gives every necesssary information about subclass developer
print(dev1.pay)
print(dev1.pay)