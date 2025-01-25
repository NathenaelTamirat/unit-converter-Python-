import sys

# Dictionary of conversion factors
conversion_dict = {
    'length': {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'micrometers': 1e6,
        'nanometers': 1e9,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    },
    'mass': {
        'grams': 1,
        'kilograms': 0.001,
        'milligrams': 1000,
        'micrograms': 1e6,
        'pounds': 0.00220462,
        'ounces': 0.035274
    },
    'temperature': {
        'celsius': ('C', 'K', lambda x: x + 273.15, lambda x: x - 273.15),
        'fahrenheit': ('F', 'K', lambda x: (x - 32) * 5/9 + 273.15, lambda x: (x - 32) * 5/9),
        'kelvin': ('K', 'C', lambda x: x - 273.15, lambda x: x)
    },
    'volume': {
        'liters': 1,
        'milliliters': 1000,
        'cubic_meters': 0.001,
        'gallons': 0.264172,
        'quarts': 1.05669,
        'pints': 2.11338,
        'cups': 4.22675,
        'fluid_ounces': 33.814
    },
    'time': {
        'seconds': 1,
        'minutes': 1/60,
        'hours': 1/3600,
        'days': 1/86400,
        'weeks': 1/604800,
        'months': 1/2628000,
        'years': 1/31536000
    }
}

def show_menu():
    """Display the main menu."""
    print("\nWelcome to the Nathenael Tamirat's Unit Converter project assingment!")
    print("Select the category of units you want to convert:")
    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Volume")
    print("5. Time")
    print("6. Exit")

def convert_units(category):
    """Handle unit conversion based on selected category."""
    if category not in conversion_dict:
        print("Invalid category.")
        return

    units = list(conversion_dict[category].keys())
    print(f"\nSelect a unit from the following list to convert from {category}:")
    for i, unit in enumerate(units, 1):
        print(f"{i}. {unit}")

    from_unit_index = int(input(f"Enter the number corresponding to the unit to convert from: ")) - 1
    from_unit = units[from_unit_index]

    print(f"\nNow select a unit to convert to {category}:")
    for i, unit in enumerate(units, 1):
        print(f"{i}. {unit}")

    to_unit_index = int(input(f"Enter the number corresponding to the unit to convert to: ")) - 1
    to_unit = units[to_unit_index]

    value = float(input(f"\nEnter the value to convert: "))
    converted_value = convert_value(value, from_unit, to_unit, category)

    print(f"\n{value} {from_unit} is equal to {converted_value} {to_unit}.\n")

def convert_value(value, from_unit, to_unit, category):
    """Convert the given value between units."""
    # If the category is temperature, handle temperature conversions with functions
    if category == 'temperature':
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return value * 9/5 + 32
            elif to_unit == 'kelvin':
                return value + 273.15
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5/9
            elif to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
    else:
        # For other categories, we use the conversion_dict
        factor_from = conversion_dict[category].get(from_unit, 1)
        factor_to = conversion_dict[category].get(to_unit, 1)
        return value * (factor_to / factor_from)

def main():
    """Main function to run the unit converter."""
    while True:
        show_menu()
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            convert_units('length')
        elif choice == 2:
            convert_units('mass')
        elif choice == 3:
            convert_units('temperature')
        elif choice == 4:
            convert_units('volume')
        elif choice == 5:
            convert_units('time')
        elif choice == 6:
            print("Exiting the program...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
