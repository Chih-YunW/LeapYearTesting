import unittest
import leapYear

class testLeapYear(unittest.TestCase):
        def test_is_a_leapYear(self):
                self.assertEqual(leapYear.leapYear(2000), "It is a leap year")
        def test_not_a_leapYear(self):
                self.assertEqual(leapYear.leapYear(1999), "It is not a leap year") 
        def test_type_error(self):
                self.assertRaises(TypeError, leapYear.leapYear, "dog") #invalid type of input

if __name__ == '__main__':
        unittest.main()

