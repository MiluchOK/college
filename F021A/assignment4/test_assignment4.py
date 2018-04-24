import unittest
from assignment4 import n2w
from num2words import num2words


class Assignment4Test(unittest.TestCase):

    def test_can_convert_all_the_nums(self):
        for number in range(-999999999, 999999999, 19153):
            print("Testing {}".format(number))
            expected = num2words(number).replace(",", "").replace("-", " ").replace(" and ", " ").strip()
            actual = n2w(number).replace("  ", " ").strip()
            self.assertEqual(expected, actual)

    def test_can_convert_small_nums(self):
        for number in range(-1999999, 1999999, 9):
            print("Testing {}".format(number))
            expected = num2words(number).replace(",", "").replace("-", " ").replace(" and ", " ").strip()
            actual = n2w(number).replace("  ", " ").strip()
            self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
