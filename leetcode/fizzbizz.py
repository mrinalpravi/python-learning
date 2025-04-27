import unittest

# class TestFizzBizz(unittest.TestCase):
#     def test_normal(self):
#         self.assertEqual(fizzbizz(15),[1, 2, 'Fizz', 4, 'Bizz', 'Fizz', 7, 8, 'Fizz', 'Bizz', 11, 'Fizz', 13, 14, 'FizzBizz'])
#     def test_negative(self):
#         with self.assertRaises(ValueError):
#             fizzbizz(-3)


def fizzbizz(nums):
    result = []
    if nums>0:
        for num in range(1, nums + 1):
            if num % 15 == 0:
                result.append("FizzBizz")
            elif num % 3 == 0:
                result.append("Fizz")
            elif num % 5 == 0:
                result.append("Bizz")
            else:
                result.append(num)
        return result
    else:
        raise ValueError


if __name__ == '__main__':
    print(fizzbizz(-5))
    # unittest.main()