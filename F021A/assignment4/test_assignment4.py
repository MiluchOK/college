import unittest
from assignment4 import n2w
from num2words import num2words


class Assignment4Test(unittest.TestCase):

    def test_can_convert_all_the_nums(self):
        for number in range(-999999999, 999999999):
            expected = num2words(number)
            actual = n2w(number)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
