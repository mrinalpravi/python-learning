import unittest

class TestSecondLargest(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(second_largest([10, 20, 30, 40, 50]), 40)

    def test_with_duplicates(self):
        self.assertEqual(second_largest([10, 20, 20, 30, 30, 40, 50]), 40)

    def test_negative_numbers(self):
        self.assertEqual(second_largest([-10, -20, -30, -40, -50]), -20)

    def test_mixed_numbers(self):
        self.assertEqual(second_largest([-1, 0, 1, 2, 3]), 2)

    def test_only_two_elements(self):
        self.assertEqual(second_largest([5, 10]), 5)

    def test_identical_numbers(self):
        with self.assertRaises(ValueError):
            second_largest([10, 10, 10])

    def test_single_element(self):
        with self.assertRaises(ValueError):
            second_largest([5])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            second_largest([])


if __name__ == '__main__':
    unittest.main()
