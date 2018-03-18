# Exercise 11-3: Employee w/ some added methods

class Employee():
    """Stores employees basic data"""

    def __init__(self, first, last, salary):
        """Stores employee first name, last name, annual salary."""
        self.first = first
        self.last = last
        self.salary = salary

    def describe_employee(self):
        employee = self.first.title() + " " + self.last.title()
        print("This employee is: " + employee + "\nSalary: " + str(self.salary))

    def give_raise(self, raises=5000):
        """Adds $5000 to the annual salary by default but can add any amount."""
        self.salary += raises

    def new_salary(self):
        """Prints an employees new salary after raise."""
        print("The new salary of this employee is: " + str(self.salary))

    # command bracket is the backward forward
