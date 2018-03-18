# Exercise 11-3: Testing!! :3

import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """
        Creates a test employee to test different methods.
        """
        self.new_employee = Employee("lauren", "havrin", 65000)

    def test_give_default_raise(self):
        """Tests if default raise of 5000 works."""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 70000)

    def test_give_custom_raise(self):
        """Test if custom raise works."""
        self.new_employee.give_raise(1000)
        self.assertEqual(self.new_employee.salary, 66000)


unittest.main()