! Weather module for the Weather program
! Western Governors University
! Created September 2024

module weather_module
  use, intrinsic :: iso_fortran_env, only : real64, int32
  implicit none
  private

  public :: Weather, new_Weather, load_weekly_weather, calculate_average_fahrenheit_high_temp, &
            calculate_average_fahrenheit_low_temp, find_weekly_fahrenheit_high_temp, &
            find_weekly_fahrenheit_low_temp, determine_description, display_today_weather, &
            display_weekly_weather

  type :: Weather
    private
    integer(int32), dimension(7) :: f_HighArray = 0
    integer(int32), dimension(7) :: f_LowArray = 0
    integer(int32) :: ws_MPH = 0
    integer(int32) :: numberTemperatures = 0
    character :: w_Code = ' '
    character(len=20) :: description = " "
  contains
    procedure :: calculate_average_fahrenheit_high_temp
    procedure :: calculate_average_fahrenheit_low_temp
    procedure :: find_weekly_fahrenheit_high_temp
    procedure :: find_weekly_fahrenheit_low_temp
    procedure :: determine_description
    procedure :: display_today_weather
    procedure :: display_weekly_weather
  end type Weather

  interface Weather
    module procedure new_Weather
  end interface Weather

contains

  function new_Weather(fhArray, flArray, arrayLengths, ws, wc) result(w)
    integer(int32), intent(in) :: fhArray(7), flArray(7), arrayLengths, ws
    character, intent(in) :: wc
    type(Weather) :: w

    w%numberTemperatures = arrayLengths
    call load_weekly_weather(w, fhArray, flArray, ws, wc)
  end function new_Weather

  subroutine load_weekly_weather(this, fhArray, flArray, ws, wc)
    class(Weather) :: this
    integer(int32), intent(in) :: fhArray(7), flArray(7), ws
    character, intent(in) :: wc

    this%f_HighArray = fhArray
    this%f_LowArray = flArray
    this%ws_MPH = ws
    this%w_Code = wc
  end subroutine load_weekly_weather

  function calculate_average_fahrenheit_high_temp(this) result(avghi)
    class(Weather), intent(in) :: this
    real(real64) :: avghi
    integer(int32) :: hisum
    
    hisum = sum(this%f_HighArray)
    avghi = real(hisum) / this%numberTemperatures
  end function calculate_average_fahrenheit_high_temp

  function calculate_average_fahrenheit_low_temp(this) result(avglow)
    class(Weather), intent(in) :: this
    real(real64) :: avglow
    integer(int32) :: lowsum

    lowsum = sum(this%f_LowArray)
    avglow = real(lowsum) / this%numberTemperatures
  end function calculate_average_fahrenheit_low_temp

  function find_weekly_fahrenheit_high_temp(this) result(highesttemp)
    class(Weather), intent(in) :: this
    integer(int32) :: highesttemp
    integer :: daycount

    highesttemp = this%f_HighArray(1)
    do daycount = 2, this%numberTemperatures
      if (this%f_HighArray(daycount) > highesttemp) then
        highesttemp = this%f_HighArray(daycount)
      end if
    end do
  end function find_weekly_fahrenheit_high_temp

  function find_weekly_fahrenheit_low_temp(this) result(lowesttemp)
    class(Weather), intent(in) :: this
    integer(int32) :: lowesttemp
    integer :: daycount

    lowesttemp = this%f_LowArray(1)
    do daycount = 2, this%numberTemperatures
      if (this%f_LowArray(daycount) < lowesttemp) then
        lowesttemp = this%f_LowArray(daycount)
      end if
    end do
  end function find_weekly_fahrenheit_low_temp

  subroutine determine_description(this)
    class(Weather) :: this

    select case (this%w_Code)
      case ('S')
        this%description = "SUNNY"
      case ('P')
        this%description = "PARTLY CLOUDY"
      case ('C')
        this%description = "CLOUDY"
      case ('N')
        this%description = "CLEAR"
    end select
  end subroutine determine_description

  subroutine display_today_weather(this)
    class(Weather) :: this

    print *, "SUNDAY FORECAST"
    print *, "High: ", this%f_HighArray(1), " (F) ", "Low: ", this%f_LowArray(1), " (F)"
    print *
  end subroutine display_today_weather

  subroutine display_weekly_weather(this)
    class(Weather) :: this
    integer(int32) :: i
    character(len=9), dimension(7), parameter :: days = [character(len=9) :: "Sunday   ", "Monday   ", "Tuesday  ", "Wednesday", &
                                                         "Thursday ", "Friday   ", "Saturday "]

    print *, "THE WEEKLY FORECAST"
    print *, "Average Hi:  ", calculate_average_fahrenheit_high_temp(this)
    print *, "Average Low: ", calculate_average_fahrenheit_low_temp(this)
    print *
    print *, "Highest Weekly Temperature: ", find_weekly_fahrenheit_high_temp(this), " (F) "
    print *, "Lowest Weekly Temperature:  ", find_weekly_fahrenheit_low_temp(this), " (F) "
    print *

    do i = 1, this%numberTemperatures
      print *, days(i)
      print *, "High: ", this%f_HighArray(i), " (F) ", "Low: ", this%f_LowArray(i), " (F)"
      print *
    end do
  end subroutine display_weekly_weather

end module weather_module
