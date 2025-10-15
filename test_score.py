# test_score.py
import unittest
from app import calculate_score

class TestScore(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(calculate_score(95), 'A')

    def test_grade_B(self):
        self.assertEqual(calculate_score(80), 'B')

    def test_grade_C(self):
        self.assertEqual(calculate_score(60), 'C')

    def test_grade_F(self):
        self.assertEqual(calculate_score(40), 'F')

if __name__ == '__main__':
    unittest.main()
