# This program is used to determine the length of a hypotenuse of a right triangle
# given two pieces of information: the nearest angle, measured in degrees, and the length of the adjacent side.

import math


# Function for inputting data.
def input_data():
    # Loop to validate useful input from nearest_angle.
    while True:
        try:
            nearest_angle = float(input("Enter the angle in degrees: "))
            if nearest_angle <= 0 or nearest_angle >= 90:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Nearest angle must be between 1 and 90. Try again.\n")

    # Loops to validate adjacent is a positive number.
    while True:
        try:
            adjacent = float(input("Enter the length of the adjacent side: "))
            if adjacent <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Try again.\n")

    return nearest_angle, adjacent


def calculate_hypotenuse(nearest_angle, adjacent):
    # Converts nearest_angle to radians (math.cos() requires radians).
    nearest_angle = math.radians(nearest_angle)

    # Calculates the length of the hypotenuse (formula used: cos(angle) = adjacent / hypotenuse).
    hypotenuse = adjacent / math.cos(nearest_angle)

    print(f"\nThe length of the hypotenuse is {hypotenuse:.2f} units.")


def main():
    print("Forewarning: Input for the nearest angle should be in DEGREES, not radians.\n")
    nearest_angle, adjacent = input_data()
    calculate_hypotenuse(nearest_angle, adjacent)


if __name__ == "__main__":
    main()
