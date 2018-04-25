import unittest
from assignment4 import spell
from num2words import num2words


class Assignment4Test(unittest.TestCase):

    def test_can_convert_all_the_nums(self):
        for number in range(-999999999, 999999999, 191531):
            expected = num2words(number).replace(",", "").replace("-", " ").replace(" and ", " ").strip()
            actual = spell(number).replace("  ", " ").strip()
            self.assertEqual(expected, actual)

    def test_can_convert_small_nums(self):
        for number in range(-1999999, 1999999, 191):
            expected = num2words(number).replace(",", "").replace("-", " ").replace(" and ", " ").strip()
            actual = spell(number).replace("  ", " ").strip()
            self.assertEqual(expected, actual)

    def test_can_convert_tiny_nums(self):
        for number in range(-99, 99):
            expected = num2words(number).replace(",", "").replace("-", " ").replace(" and ", " ").strip()
            actual = spell(number).replace("  ", " ").strip()
            self.assertEqual(expected, actual)

    def test_can_return_zero(self):
        expected = "zero"
        actual = spell(0)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
