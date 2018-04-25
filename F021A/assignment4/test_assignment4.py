import unittest
from assignment4 import spell
from num2words import num2words


class Assignment4Test(unittest.TestCase):

    def test_can_convert_all_the_nums(self):
        for number in range(-999999999, 999999999, 191531):
            expected = self.sure_convert(number)
            actual = spell(number)
            self.assertEqual(expected, actual)

    def test_can_convert_small_nums(self):
        for number in range(-1999999, 1999999, 191):
            expected = self.sure_convert(number)
            actual = spell(number)
            self.assertEqual(expected, actual)

    def test_can_convert_tiny_nums(self):
        for number in range(-99, 99):
            expected = self.sure_convert(number)
            actual = spell(number)
            self.assertEqual(expected, actual)

    def test_can_return_zero(self):
        expected = "zero"
        actual = spell(0)
        self.assertEqual(expected, actual)

    def test_can_convert_upper_boundaries(self):
        target = 999999999
        expected = self.sure_convert(target)
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_can_convert_lower_boundaries(self):
        target = -999999999
        expected = self.sure_convert(target)
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_can_raise_an_error_on_huge_input(self):
        target = 999999999 + 1
        self.assertRaises(ValueError, spell, target)

    def test_can_raise_an_error_on_small_input(self):
        target = (999999999 + 1) * -1
        self.assertRaises(ValueError, spell, target)

    def test_proffessor_example_1(self):
        target = 123456789
        expected = 'one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_2(self):
        target = 456678
        expected = 'four hundred fifty six thousand six hundred seventy eight'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_3(self):
        target = 66
        expected = 'sixty six'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_4(self):
        target = -123456789
        expected = 'negative one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_5(self):
        target = -456678
        expected = 'negative four hundred fifty six thousand six hundred seventy eight'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_6(self):
        target = -418
        expected = 'negative four hundred eighteen'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_7(self):
        target = -13456678
        expected = 'negative thirteen million four hundred fifty six thousand six hundred seventy eight'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_8(self):
        target = 0
        expected = 'zero'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def test_proffessor_example_9(self):
        target = 10004
        expected = 'ten thousand four'
        actual = spell(target)
        self.assertEqual(expected, actual)

    def sure_convert(self, num):
        return num2words(num).replace(",", "").replace("-", " ")\
            .replace(" and ", " ").replace("minus", "negative").strip()

if __name__ == '__main__':
    unittest.main()
