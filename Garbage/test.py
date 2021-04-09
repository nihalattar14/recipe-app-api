from django.test import TestCase

from app.calc import add, subtract, multiplication


class CalTest(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(5, 6), 11)

    def test_subtract_number(self):
        """Test that two numbers are subtract eachother"""
        self.assertEqual(subtract(6, 11), -5)

    def test_multiplication_number(self):
        """ Test that two numbers are multiply together"""
        self.assertEqual(multiplication(10, 20), 200)
