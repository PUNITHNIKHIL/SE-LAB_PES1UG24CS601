
import math


def parse_rental(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split(':')
    if len(parts) != 2:
        raise ValueError("Expected unit:months")

    unit, months = parts
    unit = unit.strip().title()

    if not unit:
        raise ValueError("Unit cannot be empty")

    try:
        months = float(months)
    except ValueError:
        raise ValueError("Invalid months")

    if not math.isfinite(months) or months <= 0 or not months.is_integer():
        raise ValueError("Months must be a positive whole number")

    return unit, months


def duration_average(months_csv):
    if not isinstance(months_csv, str):
        raise ValueError("Input must be a string")

    parts = months_csv.split(',')

    try:
        values = [int(x.strip()) for x in parts]
    except ValueError:
        raise ValueError("Invalid months list")

    if not values or any(x <= 0 for x in values):
        raise ValueError("Months must be positive")

    return sum(values) // len(values)


def payable_rent(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split('|')
    if len(parts) != 2:
        raise ValueError("Expected rent|discount")

    try:
        rent, discount = map(float, parts)
    except ValueError:
        raise ValueError("Invalid rent or discount")

    if not math.isfinite(rent) or not math.isfinite(discount):
        raise ValueError("Values must be finite")

    if rent < 0 or discount < 0:
        raise ValueError("Values cannot be negative")

    return max(rent * 1.18 - discount, 0)


def main():
    print("==== Running parse_rental ====")
    user_input = input("Enter unit:months (e.g. medium:6): ")
    print("Unit and Months:", parse_rental(user_input))

    print("\n==== Running duration_average ====")
    user_input = input("Enter rental months as CSV (e.g. 3,6,12): ")
    print("Average Duration:", duration_average(user_input))

    print("\n==== Running payable_rent ====")
    user_input = input("Enter rent|discount (e.g. 2400|200): ")
    print("Payable Rent:", payable_rent(user_input))


if __name__ == "__main__":
    main()
