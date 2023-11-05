import unittest
from math_quiz import random_num, random_operator, mathOperator_path


class TestMathGame(unittest.TestCase):

    def test_random_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_num(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # TODO
        # Test that the chosen operator is one of the expected operators
        operator = random_operator()
        self.assertIn(operator, ['+', '-', '*'])

    def test_mathOperator_path(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                #''' TODO add more test cases here '''
                (3, 7, '-', '3 - 7', -4),
                (6, 6, '*', '6 * 6', 36),
                (10, 5, '+', '10 + 5', 15),
                (8, 4, '-', '8 - 4', 4),
                (9, 3, '*', '9 * 3', 27)
            ]

            for num1, num2, operator, expected_problem, expected_result in test_cases:
                # TODO
                 problem, result = mathOperator_path(num1, num2, operator)
                 self.assertEqual(problem, expected_problem)
                 self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
