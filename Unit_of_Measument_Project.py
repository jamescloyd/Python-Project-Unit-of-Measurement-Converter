# This is the logic behind my unit of measurement converter

# Ask the user what unit of measurement they want to convert from and what unit of measurement they want to convert to
convert_from = input("Enter Starting Unit of Measurement (inches, feet, or yards): ")
convert_to = input("Enter Unit of Measurement to Convert to (inches, feet, or yards): ")

# Convert from "inches" to "feet" or "yards"
if convert_from.lower() in ["inches", "in", "inch"]:  # ".lower()" makes sure that no matter how the user types the unit of measurement, the converter is able to capture it.
    number_of_inches = float(input("Enter Starting Measurement in Inches: "))  # We need to convert it to a float because Python condiders this a string.
    if convert_to.lower() in ["feet", "ft", "foot"]:
        print("Result: " + str(number_of_inches) + " Inches = " + str(round(number_of_inches / 12, 2)) + " Feet")
    elif convert_to.lower() in ["yards", "yard", "yd", "yds"]:
        print("Result: " + str(number_of_inches) + " Inches = " + str(round(number_of_inches / 36, 2)) + " Yards")
    else:
        print('Please enter the Unit of Measurement to Convert to either as "Feet" or "Yards".')
# Convert from "feet" to "inches" or "yards"
elif convert_from.lower() in ["feet", "ft", "foot"]:
    number_of_feet = float(input("Enter Starting Measurement in Feet: "))
    if convert_to.lower() in ["inches", "in", "inch"]:
        print("Result: " + str(number_of_feet) + " Feet = " + str(round(number_of_feet * 12, 2)) + " Inches")
    elif convert_to.lower() in ["yards", "yard", "yd", "yds"]:
        print("Result: " + str(number_of_feet) + " Feet = " + str(round(number_of_feet / 3, 2)) + " Yards")
    else:
        print('Please enter the Unit of Measurement to Convert to either as "Inches" or "Yards".')
# Convert from "yards" to "inches" or "feet"
elif convert_from.lower() in ["yards", "yard", "yd", "yds"]:
    number_of_yards = float(input("Enter Starting Measurement in Yards: "))
    if convert_to.lower() in ["inches", "in", "inch"]:
        print("Result: " + str(number_of_yards) + " Yards = " + str(round(number_of_yards * 36, 2)) + " Inches")
    elif convert_to.lower() in ["feet", "ft", "foot"]:
        print("Result: " + str(number_of_yards) + " Yards = " + str(round(number_of_yards * 3, 2)) + " Feet")
    else:
        print('Please enter the Unit of Measurement to Convert to either as "Inches" or "Feet".')
else:
    print('Please enter the Unit of Measurement either as "Inches", "Feet", or "Yards".')
