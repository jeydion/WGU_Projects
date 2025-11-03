# Makefile for Weather Program
# Compiler
FC = gfortran
# Compiler flags (optional, but good practice)
FFLAGS = -Wall -std=f2008

# Target executable name
TARGET = weather_program

# Source files
SOURCES = weather.f90 main.f90

# Default target - what happens when you type "make"
all: $(TARGET)

# How to build the executable
$(TARGET): $(SOURCES)
	$(FC) $(FFLAGS) $(SOURCES) -o $(TARGET)

# Clean up compiled files
clean:
	rm -f *.o *.mod $(TARGET)

# Run the program
run: $(TARGET)
	./$(TARGET)