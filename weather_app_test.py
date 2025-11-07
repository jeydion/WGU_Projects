#!/usr/bin/env python3
"""
Unit tests for the Weather program
Tests core temperature calculations and edge cases
Western Governors University
Created November 2025
"""

import unittest
from weather import Weather


class TestWeatherProgram(unittest.TestCase):
    """
    Comprehensive Test Suite for Weather Program
    
    This test suite focuses on:
    1. Core temperature calculation functionality
    2. Edge cases including extreme values and boundary conditions
    
    Each test includes detailed output showing processing status and results.
    """
    
    def setUp(self):
        """
        Set up standard test data before each test method runs.
        
        Standard test data represents a typical week with:
        - High temperatures ranging from 85°F to 92°F
        - Low temperatures ranging from 60°F to 68°F
        """
        print("\n" + "="*70)
        self.highs = [90, 85, 88, 92, 87, 89, 91]
        self.lows = [65, 60, 63, 68, 62, 64, 66]
    
    def test_1_average_temperature_calculations(self):
        """
        Test 1: Verify Average Temperature Calculations
        
        This test ensures that the Weather class correctly calculates
        the average high and average low temperatures across a 7-day period.
        
        Mathematical verification:
        - Average High: (90+85+88+92+87+89+91) / 7 = 622 / 7 = 88.857°F
        - Average Low: (65+60+63+68+62+64+66) / 7 = 448 / 7 = 64.0°F
        """
        print("TEST 1: Processing average temperature calculations...")
        print(f"  Input Data - Highs: {self.highs}")
        print(f"  Input Data - Lows: {self.lows}")
        
        weather = Weather(self.highs, self.lows, 7, 10, 'S')
        
        # Test average high
        expected_avg_high = 88.857142857
        actual_avg_high = weather.calculate_average_fahrenheit_high_temp()
        print(f"  Expected Average High: {expected_avg_high:.2f}°F")
        print(f"  Actual Average High: {actual_avg_high:.2f}°F")
        
        # Test average low
        expected_avg_low = 64.0
        actual_avg_low = weather.calculate_average_fahrenheit_low_temp()
        print(f"  Expected Average Low: {expected_avg_low:.2f}°F")
        print(f"  Actual Average Low: {actual_avg_low:.2f}°F")
        
        self.assertAlmostEqual(actual_avg_high, expected_avg_high, places=2,
                              msg="Average high temperature calculation is incorrect")
        self.assertAlmostEqual(actual_avg_low, expected_avg_low, places=2,
                              msg="Average low temperature calculation is incorrect")
        
        print("  ✓ PASS: Average temperature calculations are correct")
    
    def test_2_min_max_temperature_finding(self):
        """
        Test 2: Verify Min/Max Temperature Detection
        
        This test ensures that the Weather class correctly identifies
        the highest and lowest temperatures from the weekly data.
        
        Verification:
        - Maximum high should be 92°F (from day 4)
        - Minimum low should be 60°F (from day 2)
        """
        print("TEST 2: Processing min/max temperature detection...")
        print(f"  Input Data - Highs: {self.highs}")
        print(f"  Input Data - Lows: {self.lows}")
        
        weather = Weather(self.highs, self.lows, 7, 10, 'S')
        
        # Test maximum high
        expected_max = 92
        actual_max = weather.find_weekly_fahrenheit_high_temp()
        print(f"  Expected Maximum High: {expected_max}°F")
        print(f"  Actual Maximum High: {actual_max}°F")
        
        # Test minimum low
        expected_min = 60
        actual_min = weather.find_weekly_fahrenheit_low_temp()
        print(f"  Expected Minimum Low: {expected_min}°F")
        print(f"  Actual Minimum Low: {actual_min}°F")
        
        self.assertEqual(actual_max, expected_max,
                        msg=f"Expected highest temp {expected_max}, got {actual_max}")
        self.assertEqual(actual_min, expected_min,
                        msg=f"Expected lowest temp {expected_min}, got {actual_min}")
        
        print("  ✓ PASS: Min/max temperature detection is correct")
    
    def test_3_extreme_cold_temperatures(self):
        """
        Test 3: Handle Extreme Cold (Negative) Temperatures
        
        This test verifies that the Weather class correctly processes
        extreme cold conditions, including negative temperatures.
        
        Test scenario: Arctic winter conditions
        - High temperatures: 10°F down to 5°F
        - Low temperatures: -5°F down to -15°F
        
        This tests the robustness of mathematical operations with
        negative values and ensures no integer overflow issues.
        """
        print("TEST 3: Processing extreme cold temperature handling...")
        
        cold_highs = [10, 5, 8, 12, 7, 9, 6]
        cold_lows = [-10, -15, -8, -5, -12, -9, -11]
        
        print(f"  Extreme Cold Highs: {cold_highs}")
        print(f"  Extreme Cold Lows: {cold_lows}")
        
        weather = Weather(cold_highs, cold_lows, 7, 20, 'C')
        
        # Test minimum low with negative temperatures
        expected_min = -15
        actual_min = weather.find_weekly_fahrenheit_low_temp()
        print(f"  Expected Minimum Low: {expected_min}°F")
        print(f"  Actual Minimum Low: {actual_min}°F")
        
        # Test average low with negative temperatures
        expected_avg_low = -10.0
        actual_avg_low = weather.calculate_average_fahrenheit_low_temp()
        print(f"  Expected Average Low: {expected_avg_low:.2f}°F")
        print(f"  Actual Average Low: {actual_avg_low:.2f}°F")
        
        self.assertEqual(actual_min, expected_min,
                        msg=f"Failed to handle negative temperatures correctly")
        self.assertAlmostEqual(actual_avg_low, expected_avg_low, places=2,
                              msg="Average calculation failed with negative values")
        
        print("  ✓ PASS: Extreme cold temperatures handled correctly")
    
    def test_4_extreme_hot_temperatures(self):
        """
        Test 4: Handle Extreme Heat Temperatures
        
        This test verifies that the Weather class correctly processes
        extreme heat conditions near or above 120°F.
        
        Test scenario: Desert summer conditions
        - High temperatures: 115°F to 122°F
        - Low temperatures: 90°F to 98°F
        
        This ensures the program can handle upper boundary conditions
        without mathematical errors or precision issues.
        """
        print("TEST 4: Processing extreme heat temperature handling...")
        
        extreme_highs = [120, 115, 118, 122, 119, 121, 117]
        extreme_lows = [95, 90, 93, 98, 94, 96, 92]
        
        print(f"  Extreme Heat Highs: {extreme_highs}")
        print(f"  Extreme Heat Lows: {extreme_lows}")
        
        weather = Weather(extreme_highs, extreme_lows, 7, 15, 'S')
        
        # Test maximum high with extreme values
        expected_max = 122
        actual_max = weather.find_weekly_fahrenheit_high_temp()
        print(f"  Expected Maximum High: {expected_max}°F")
        print(f"  Actual Maximum High: {actual_max}°F")
        
        # Test minimum low
        expected_min = 90
        actual_min = weather.find_weekly_fahrenheit_low_temp()
        print(f"  Expected Minimum Low: {expected_min}°F")
        print(f"  Actual Minimum Low: {actual_min}°F")
        
        # Test average high with extreme values
        expected_avg_high = 118.857
        actual_avg_high = weather.calculate_average_fahrenheit_high_temp()
        print(f"  Expected Average High: {expected_avg_high:.2f}°F")
        print(f"  Actual Average High: {actual_avg_high:.2f}°F")
        
        self.assertEqual(actual_max, expected_max,
                        msg="Failed to find maximum in extreme heat conditions")
        self.assertEqual(actual_min, expected_min,
                        msg="Failed to find minimum in extreme heat conditions")
        self.assertAlmostEqual(actual_avg_high, expected_avg_high, places=2,
                              msg="Average calculation failed with extreme heat values")
        
        print("  ✓ PASS: Extreme heat temperatures handled correctly")
    
    def test_5_data_isolation_and_integrity(self):
        """
        Test 5: Verify Data Isolation and Integrity
        
        This test ensures that the Weather class creates independent copies
        of input data, preventing external modifications from affecting
        the Weather object's internal state.
        
        Test procedure:
        1. Create Weather object with initial arrays
        2. Modify the original input arrays
        3. Verify Weather object remains unchanged
        
        This is critical for data integrity and preventing side effects
        in programs that reuse array variables.
        """
        print("TEST 5: Processing data isolation and integrity test...")
        
        original_highs = [80, 81, 82, 83, 84, 85, 86]
        original_lows = [60, 61, 62, 63, 64, 65, 66]
        
        print(f"  Original Highs: {original_highs}")
        print(f"  Original Lows: {original_lows}")
        
        # Create Weather object
        weather = Weather(original_highs, original_lows, 7, 10, 'S')
        
        print("  Creating Weather object with original data...")
        print(f"  Initial Max High: {weather.find_weekly_fahrenheit_high_temp()}°F")
        print(f"  Initial Min Low: {weather.find_weekly_fahrenheit_low_temp()}°F")
        
        # Modify original arrays (attempting to corrupt data)
        print("\n  ⚠ Modifying original arrays externally...")
        original_highs[0] = 999
        original_lows[0] = -999
        print(f"  Modified Highs: {original_highs}")
        print(f"  Modified Lows: {original_lows}")
        
        # Verify Weather object is unaffected
        expected_max = 86
        actual_max = weather.find_weekly_fahrenheit_high_temp()
        expected_min = 60
        actual_min = weather.find_weekly_fahrenheit_low_temp()
        
        print(f"\n  Weather Object Max High (should be unchanged): {actual_max}°F")
        print(f"  Weather Object Min Low (should be unchanged): {actual_min}°F")
        
        self.assertEqual(actual_max, expected_max,
                        msg="Weather object was affected by external array modification (highs)")
        self.assertEqual(actual_min, expected_min,
                        msg="Weather object was affected by external array modification (lows)")
        
        print("  ✓ PASS: Data isolation maintained - Weather object unaffected by external changes")


def run_tests():
    """
    Custom test runner with enhanced output formatting.
    
    This function:
    1. Creates a test suite with all test methods
    2. Runs tests with detailed verbosity
    3. Provides a comprehensive summary of results
    """
    print("\n" + "="*70)
    print("WEATHER PROGRAM - UNIT TEST SUITE")
    print("="*70)
    print("Running 5 comprehensive tests covering:")
    print("  • Core temperature calculation functionality")
    print("  • Edge cases with extreme values")
    print("  • Data integrity and isolation")
    print("="*70)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestWeatherProgram)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print detailed summary
    print("\n" + "="*70)
    print("FINAL TEST SUMMARY")
    print("="*70)
    print(f"Total Tests Run: {result.testsRun}")
    print(f"✓ Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"✗ Failures: {len(result.failures)}")
    print(f"⚠ Errors: {len(result.errors)}")
    print("="*70)
    
    if result.wasSuccessful():
        print("🎉 ALL TESTS PASSED! Weather program is functioning correctly.")
    else:
        print("⚠ SOME TESTS FAILED. Please review the output above.")
    
    print("="*70 + "\n")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    # Run tests when script is executed directly
    success = run_tests()
    
    # Exit with appropriate code (0 = success, 1 = failure)
    exit(0 if success else 1)