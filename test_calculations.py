# test_calculations.py
# Test cases for calculation logic
import unittest
from calculations import calculate_needed_score

class TestCalculations(unittest.TestCase):
    def test_calculate_needed_score(self):
        self.assertAlmostEqual(calculate_needed_score(85, 0.4, 90), 95)
        self.assertAlmostEqual(calculate_needed_score(70, 0.5, 80), 90)

if __name__ == "__main__":
    unittest.main()