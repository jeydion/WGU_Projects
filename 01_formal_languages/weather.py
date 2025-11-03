"""
Weather module for the Weather program
Translated from Fortran to Python
Western Governors University
Created November 2024
"""

from typing import List


class Weather:
    """
    Weather class to store and analyze weekly weather data.
    
    This class encapsulates weather information including high/low temperatures,
    wind speed, and weather conditions. It provides methods to calculate
    statistics and display weather forecasts.
    
    Attributes:
        _f_high_array (List[int]): Array of 7 daily high temperatures in Fahrenheit
        _f_low_array (List[int]): Array of 7 daily low temperatures in Fahrenheit
        _ws_mph (int): Wind speed in miles per hour
        _number_temperatures (int): Number of temperature readings (always 7 for weekly)
        _w_code (str): Weather code ('S'=Sunny, 'P'=Partly Cloudy, 'C'=Cloudy, 'N'=Clear)
        _description (str): Human-readable weather description
    """
    
    def __init__(self, fh_array: List[int], fl_array: List[int], 
                 array_lengths: int, ws: int, wc: str):
        """
        Initialize Weather object with temperature and weather data.
        
        Args:
            fh_array: List of 7 high temperatures in Fahrenheit
            fl_array: List of 7 low temperatures in Fahrenheit
            array_lengths: Number of temperature readings (should be 7)
            ws: Wind speed in miles per hour
            wc: Weather code character
        """
        # Private attributes (indicated by leading underscore)
        self._f_high_array: List[int] = [0] * 7
        self._f_low_array: List[int] = [0] * 7
        self._ws_mph: int = 0
        self._number_temperatures: int = array_lengths
        self._w_code: str = ' '
        self._description: str = ""
        
        # Load the weekly weather data
        self._load_weekly_weather(fh_array, fl_array, ws, wc)
    
    def _load_weekly_weather(self, fh_array: List[int], fl_array: List[int], 
                            ws: int, wc: str) -> None:
        """
        Load weekly weather data into the object.
        
        Args:
            fh_array: High temperatures
            fl_array: Low temperatures
            ws: Wind speed
            wc: Weather code
        """
        self._f_high_array = fh_array.copy()  # Create a copy to avoid reference issues
        self._f_low_array = fl_array.copy()
        self._ws_mph = ws
        self._w_code = wc
    
    def calculate_average_fahrenheit_high_temp(self) -> float:
        """
        Calculate the average of all high temperatures for the week.
        
        Returns:
            float: Average high temperature
        """
        hi_sum = sum(self._f_high_array)
        avg_hi = hi_sum / self._number_temperatures
        return avg_hi
    
    def calculate_average_fahrenheit_low_temp(self) -> float:
        """
        Calculate the average of all low temperatures for the week.
        
        Returns:
            float: Average low temperature
        """
        low_sum = sum(self._f_low_array)
        avg_low = low_sum / self._number_temperatures
        return avg_low
    
    def find_weekly_fahrenheit_high_temp(self) -> int:
        """
        Find the highest temperature in the week.
        
        Returns:
            int: Highest temperature value
        """
        highest_temp = self._f_high_array[0]
        for temp in self._f_high_array[1:]:
            if temp > highest_temp:
                highest_temp = temp
        return highest_temp
        # Alternative Pythonic way: return max(self._f_high_array)
    
    def find_weekly_fahrenheit_low_temp(self) -> int:
        """
        Find the lowest temperature in the week.
        
        Returns:
            int: Lowest temperature value
        """
        lowest_temp = self._f_low_array[0]
        for temp in self._f_low_array[1:]:
            if temp < lowest_temp:
                lowest_temp = temp
        return lowest_temp
        # Alternative Pythonic way: return min(self._f_low_array)
    
    def determine_description(self) -> None:
        """
        Determine the weather description based on the weather code.
        
        Updates the internal _description attribute based on _w_code:
            'S' -> "SUNNY"
            'P' -> "PARTLY CLOUDY"
            'C' -> "CLOUDY"
            'N' -> "CLEAR"
        """
        # Dictionary mapping (more Pythonic than if-elif)
        code_map = {
            'S': "SUNNY",
            'P': "PARTLY CLOUDY",
            'C': "CLOUDY",
            'N': "CLEAR"
        }
        self._description = code_map.get(self._w_code, "UNKNOWN")
    
    def display_today_weather(self) -> None:
        """
        Display today's (Sunday's) weather forecast.
        
        Prints the high and low temperature for the first day in the arrays.
        """
        print("SUNDAY FORECAST")
        print(f"High: {self._f_high_array[0]} (F)  Low: {self._f_low_array[0]} (F)")
        print()
    
    def display_weekly_weather(self) -> None:
        """
        Display the complete weekly weather forecast.
        
        Shows:
        - Average high and low temperatures
        - Highest and lowest weekly temperatures
        - Daily forecast for each day of the week
        """
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday", "Saturday"]
        
        print("THE WEEKLY FORECAST")
        print(f"Average Hi:  {self.calculate_average_fahrenheit_high_temp():.2f}")
        print(f"Average Low: {self.calculate_average_fahrenheit_low_temp():.2f}")
        print()
        print(f"Highest Weekly Temperature: {self.find_weekly_fahrenheit_high_temp()} (F)")
        print(f"Lowest Weekly Temperature:  {self.find_weekly_fahrenheit_low_temp()} (F)")
        print()
        
        for i in range(self._number_temperatures):
            print(days[i])
            print(f"High: {self._f_high_array[i]} (F)  Low: {self._f_low_array[i]} (F)")
            print()


# Public functions that can be used outside the class
def new_weather(fh_array: List[int], fl_array: List[int], 
                array_lengths: int, ws: int, wc: str) -> Weather:
    """
    Factory function to create a new Weather object.
    
    This mimics the Fortran interface pattern where Weather() 
    calls new_Weather() internally.
    
    Args:
        fh_array: High temperatures
        fl_array: Low temperatures
        array_lengths: Number of readings
        ws: Wind speed
        wc: Weather code
    
    Returns:
        Weather: New Weather object
    """
    return Weather(fh_array, fl_array, array_lengths, ws, wc)
