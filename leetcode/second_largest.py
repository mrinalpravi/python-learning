import unittest
import csv

def second_largest(numbers):
    numbers.sort()
    unique_numbers = list(set(numbers))

    if len(numbers)>2:
        return numbers[-2]
    elif len(unique_numbers) < len(numbers):
        raise ValueError("Duplicate present")
    else:
        raise ValueError("Only 1 element")



class SecondLargestTest(unittest.TestCase):
    def test_common(self):
        self.assertEqual(second_largest([1,2,4,6]),4)
    def test_negative(self):
        self.assertEqual(second_largest([-1,-2,-3,-10]),-2)
    def test_duplicate(self):
        with self.assertRaises(ValueError):
            second_largest([12,12,10,23])
    def test_errorcase(self):
        with self.assertRaises(ValueError):
            second_largest([1])




if __name__ == '__main__':
    print(second_largest([23,43,1,24]))
    unittest.main()


