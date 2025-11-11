! Main file to start the weather console-based program
! Western Governors University
! Created September 2024

program weather_program
  use weather_module 

  implicit none

  ! Main variables
  ! fh = Fahrenheit High
  ! fl = Fahrenheit Low
  ! ws = Wind Speed in MPH
  ! wc = Weather Code
  integer, dimension(7) :: fh = (/ 78, 76, 80, 82, 85, 79, 75 /)
  integer, dimension(7) :: fl = (/ 75, 70, 75, 76, 75, 70, 69 /)
  integer :: ws = 9
  integer, parameter :: numberTemperatures = 7 ! The number of temperatures is the same for the high and low temperature array lengths
  character :: wc = 'P'
  type(Weather) :: w

  ! Initialize Weather type
  w = Weather(fh, fl, numberTemperatures, ws, wc)

  ! Call procedures to determine and display weather information
  call determine_description(w)
  call display_today_weather(w)
  call display_weekly_weather(w)

end program weather_program