import unittest
from app import calculate_bmi  # Replace with the actual function name in your app.py file

class TestBMICalculator(unittest.TestCase):
    def test_bmi_kg_m(self):
        """Test BMI calculation with weight in kg and height in meters."""
        self.assertAlmostEqual(calculate_bmi(70, "kg", 1.75, "m"), 22.86, places=2)

    def test_bmi_lb_ft(self):
        """Test BMI calculation with weight in lbs and height in feet."""
        self.assertAlmostEqual(calculate_bmi(154, "lbs", 5.9, "ft"), 21.60, places=2)

    def test_bmi_g_cm(self):
        """Test BMI calculation with weight in grams and height in cm."""
        self.assertAlmostEqual(calculate_bmi(70000, "g", 175, "cm"), 22.86, places=2)

    def test_invalid_height(self):
        """Test error handling for invalid height."""
        with self.assertRaises(ValueError):
            calculate_bmi(70, "kg", 0, "m")  # Height cannot be zero

    def test_invalid_weight(self):
        """Test error handling for invalid weight."""
        with self.assertRaises(ValueError):
            calculate_bmi(0, "kg", 1.75, "m")  # Weight cannot be zero

if __name__ == "__main__":
    unittest.main()
