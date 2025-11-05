#!/usr/bin/env python3
"""
Unit tests for the Weather program
Tests temperature calculations, weather code mappings, and edge cases
Western Governors University
Created November 2025
"""

import unittest
from weather import Weather


class TestTemperatureCalculations(unittest.TestCase):
    """
    Test Suite 1: Temperature Calculation Accuracy
    
    Tests the core mathematical functions for calculating averages
    and finding min/max temperatures.
    """
    
    def setUp(self):
        """Set up test data before each test method runs"""
        self.highs = [90, 85, 88, 92, 87, 89, 91]
        self.lows = [65, 60, 63, 68, 62, 64, 66]
        self.weather = Weather(self.highs, self.lows, 7, 10, 'S')
    
    def test_average_high_temperature(self):
        """Test that average high temperature is calculated correctly"""
        expected = 88.857142857  # Sum: 622 / 7
        actual = self.weather.calculate_average_fahrenheit_high_temp()
        self.assertAlmostEqual(actual, expected, places=2,
                              msg="Average high temperature calculation is incorrect")
    
    def test_average_low_temperature(self):
        """Test that average low temperature is calculated correctly"""
        expected = 64.0  # Sum: 448 / 7
        actual = self.weather.calculate_average_fahrenheit_low_temp()
        self.assertAlmostEqual(actual, expected, places=2,
                              msg="Average low temperature calculation is incorrect")
    
    def test_find_highest_temperature(self):
        """Test that the highest temperature in the week is found correctly"""
        expected = 92
        actual = self.weather.find_weekly_fahrenheit_high_temp()
        self.assertEqual(actual, expected,
                        msg=f"Expected highest temp {expected}, got {actual}")
    
    def test_find_lowest_temperature(self):
        """Test that the lowest temperature in the week is found correctly"""
        expected = 60
        actual = self.weather.find_weekly_fahrenheit_low_temp()
        self.assertEqual(actual, expected,
                        msg=f"Expected lowest temp {expected}, got {actual}")


class TestWeatherCodeDescriptions(unittest.TestCase):
    """
    Test Suite 2: Weather Code to Description Mapping
    
    Tests that weather codes are correctly mapped to their
    human-readable descriptions.
    """
    
    def setUp(self):
        """Set up basic weather data (temperatures don't matter for these tests)"""
        self.highs = [75, 75, 75, 75, 75, 75, 75]
        self.lows = [60, 60, 60, 60, 60, 60, 60]
    
    def test_sunny_code(self):
        """Test that 'S' code maps to 'SUNNY'"""
        weather = Weather(self.highs, self.lows, 7, 5, 'S')
        weather.determine_description()
        self.assertEqual(weather._description, "SUNNY",
                        msg="Weather code 'S' should map to 'SUNNY'")
    
    def test_partly_cloudy_code(self):
        """Test that 'P' code maps to 'PARTLY CLOUDY'"""
        weather = Weather(self.highs, self.lows, 7, 5, 'P')
        weather.determine_description()
        self.assertEqual(weather._description, "PARTLY CLOUDY",
                        msg="Weather code 'P' should map to 'PARTLY CLOUDY'")
    
    def test_cloudy_code(self):
        """Test that 'C' code maps to 'CLOUDY'"""
        weather = Weather(self.highs, self.lows, 7, 5, 'C')
        weather.determine_description()
        self.assertEqual(weather._description, "CLOUDY",
                        msg="Weather code 'C' should map to 'CLOUDY'")
    
    def test_clear_code(self):
        """Test that 'N' code maps to 'CLEAR'"""
        weather = Weather(self.highs, self.lows, 7, 5, 'N')
        weather.determine_description()
        self.assertEqual(weather._description, "CLEAR",
                        msg="Weather code 'N' should map to 'CLEAR'")
    
    def test_invalid_code(self):
        """Test that an invalid code maps to 'UNKNOWN'"""
        weather = Weather(self.highs, self.lows, 7, 5, 'X')
        weather.determine_description()
        self.assertEqual(weather._description, "UNKNOWN",
                        msg="Invalid weather code should map to 'UNKNOWN'")


class TestEdgeCasesAndDataIntegrity(unittest.TestCase):
    """
    Test Suite 3: Edge Cases and Data Integrity
    
    Tests robustness with extreme values, data isolation,
    and boundary conditions.
    """
    
    def test_extreme_hot_temperatures(self):
        """Test handling of extremely high temperatures"""
        extreme_highs = [120, 115, 118, 122, 119, 121, 117]
        extreme_lows = [95, 90, 93, 98, 94, 96, 92]
        weather = Weather(extreme_highs, extreme_lows, 7, 15, 'S')
        
        # Should handle extreme values without crashing
        self.assertEqual(weather.find_weekly_fahrenheit_high_temp(), 122)
        self.assertEqual(weather.find_weekly_fahrenheit_low_temp(), 90)
        self.assertAlmostEqual(weather.calculate_average_fahrenheit_high_temp(), 118.857, places=2)
    
    def test_extreme_cold_temperatures(self):
        """Test handling of extremely low (negative) temperatures"""
        cold_highs = [10, 5, 8, 12, 7, 9, 6]
        cold_lows = [-10, -15, -8, -5, -12, -9, -11]
        weather = Weather(cold_highs, cold_lows, 7, 20, 'C')
        
        # Should handle negative values correctly
        self.assertEqual(weather.find_weekly_fahrenheit_low_temp(), -15)
        self.assertAlmostEqual(weather.calculate_average_fahrenheit_low_temp(), -10.0, places=2)
    
    def test_data_isolation(self):
        """Test that modifying original arrays doesn't affect Weather object"""
        original_highs = [80, 81, 82, 83, 84, 85, 86]
        original_lows = [60, 61, 62, 63, 64, 65, 66]
        
        # Create Weather object
        weather = Weather(original_highs, original_lows, 7, 10, 'S')
        
        # Modify original arrays
        original_highs[0] = 999
        original_lows[0] = -999
        
        # Weather object should be unaffected
        self.assertEqual(weather.find_weekly_fahrenheit_high_temp(), 86,
                        msg="Weather object was affected by external array modification")
        self.assertEqual(weather.find_weekly_fahrenheit_low_temp(), 60,
                        msg="Weather object was affected by external array modification")
    
    def test_uniform_temperatures(self):
        """Test when all temperatures are identical"""
        uniform_highs = [75, 75, 75, 75, 75, 75, 75]
        uniform_lows = [60, 60, 60, 60, 60, 60, 60]
        weather = Weather(uniform_highs, uniform_lows, 7, 5, 'P')
        
        # Average, min, and max should all be the same value
        self.assertEqual(weather.calculate_average_fahrenheit_high_temp(), 75.0)
        self.assertEqual(weather.find_weekly_fahrenheit_high_temp(), 75)
        self.assertEqual(weather.find_weekly_fahrenheit_low_temp(), 60)
    
    def test_all_seven_days_processed(self):
        """Test that all 7 days are correctly stored and processed"""
        highs = [70, 71, 72, 73, 74, 75, 76]
        lows = [50, 51, 52, 53, 54, 55, 56]
        weather = Weather(highs, lows, 7, 8, 'N')
        
        # Verify internal arrays have all 7 values
        self.assertEqual(len(weather._f_high_array), 7)
        self.assertEqual(len(weather._f_low_array), 7)
        
        # Verify correct values at boundaries
        self.assertEqual(weather._f_high_array[0], 70)  # First day
        self.assertEqual(weather._f_high_array[6], 76)  # Last day
        self.assertEqual(weather._f_low_array[0], 50)
        self.assertEqual(weather._f_low_array[6], 56)


def run_tests():
    """
    Run all test suites and display results.
    """
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestTemperatureCalculations))
    suite.addTests(loader.loadTestsFromTestCase(TestWeatherCodeDescriptions))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCasesAndDataIntegrity))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    # Run tests when script is executed directly
    success = run_tests()
    
    # Exit with appropriate code (0 = success, 1 = failure)
    exit(0 if success else 1)