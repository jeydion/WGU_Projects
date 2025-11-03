#!/usr/bin/env python3
"""
Main file to start the weather console-based program
Translated from Fortran to Python
Western Governors University
Created November 2024
"""

from weather import Weather


def main():
    """
    Main entry point for the weather program.
    
    Creates a Weather object with sample data and displays
    both today's and the weekly weather forecast.
    """
    # Main variables
    # fh = Fahrenheit High
    # fl = Fahrenheit Low
    # ws = Wind Speed in MPH
    # wc = Weather Code
    fh = [78, 76, 80, 82, 85, 79, 75]
    fl = [75, 70, 75, 76, 75, 70, 69]
    ws = 9
    number_temperatures = 7  # The number of temperatures in the arrays
    wc = 'P'
    
    # Initialize Weather object
    w = Weather(fh, fl, number_temperatures, ws, wc)
    
    # Call methods to determine and display weather information
    w.determine_description()
    w.display_today_weather()
    w.display_weekly_weather()


if __name__ == "__main__":
    # This block only runs if the script is executed directly
    # (not when imported as a module)
    main()
