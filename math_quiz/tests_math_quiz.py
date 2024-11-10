import unittest
from math_quiz import integergeneration, opterationgeneration, questiongeneration


class TestMathGame(unittest.TestCase):

    def test_integergeneration(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = integergeneration(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_opterationgeneration(self):
      
        operators = ['+', '-', '*']
        for _ in range(1000):
            operator = randomOperatorGenerator()
            self.assertIn(operator, operators)
        

    def test_questiongeneration(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 7, '-', '8 - 7', 1),
                (7, 3, '*', '7 * 3', 21),
                (5, 9, '+', '3 + 9', 14),
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                
                question, result = questiongeneration(num1, num2, operator)
                self.assertEqual(question, expected_problem)
                self.assertEqual(result, expected_answer)
               

if __name__ == "__main__":
    unittest.main()
