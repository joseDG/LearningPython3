
# Employees Project
# Study the code and compare to yours
# Observe how I try to create meaningful classes that help organize the code
# This is a very important skill: To view the world as interacting objects

def input_valid_int(msg, start = 0, end = None):
    # keep iterating till the given input is valid
    # hidden assumption: both start and end either value or none. That is bad
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
                # another way is to check if int(inp) in range(start, end+1)
            else:
                return int(inp)
        else:
            return int(inp)


class Employee:
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary

    def __str__(self):
        return f'Employee: {self.name} has age {self.age} and salary {self.salary}'

    def __repr__(self):
        return F'Employee(name="{self.name}", age={self.age}, salary={self.salary})'


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('\nEnter employee data:')
        name = input('Enter the name: ')
        age = input_valid_int('Enter the age: ')
        salary = input_valid_int('Enter the salary: ')

        self.employees.append(Employee(name, age, salary))

    def list_emplyoees(self):
        if len(self.employees) == 0:
            print('\nNo employees at the moment!')
            return

        print('\n**Employees list**')
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        # remove from the back!
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print('\tDeleting', emp.name)
                self.employees.pop(idx)

        # Tip - pop from middle of a list is slow! O(n)
        # One trick to make things efficient is as following
        # for every item to delete swap with the end of the list
        # e.g. if we will delete 3 items swap them to be the last 3 elements in list
        # now delete the last 3 elements
        # pros: very efficient
        # cons: we altered the list order. It depends then on the app!

        # Another easier trick is to mark the removed person with None
        # if there is a new employee to add, just put him in one of the None
        # this way complete no deletion at all!
        # you can have another playlist with None locations
        # cons: if there are many removed employees, you iterate a lot
        # workaround: after somethreshold: recreate a new fresh employees list

        # if you don't get above tricks, that is ok for now :)
        # it takes time to be a problem-solver

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)

        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary = salary

class FrontendManager:
    def __init__(self):
        self.employees_manger = EmployeesManager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manger.add_employee()
            elif choice == 2:
                self.employees_manger.list_emplyoees()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')
                # for simplicity: I assume no input such as 60 30_oop , but valid one: 30_oop 60 (small large)
                self.employees_manger.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = input_valid_int('Enter new salary: ')
                self.employees_manger.update_salary_by_name(name, salary)
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()
