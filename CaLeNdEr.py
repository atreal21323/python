import calendar
import datetime

MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def print_month_names():
    print("Months of the year:")
    for index, name in enumerate(MONTH_NAMES, start=1):
        print(f"{index:2d}. {name}")
    print()


def print_year_calendar(year):
    print(f"\nCalendar for {year}:\n")
    print(calendar.calendar(year))


def print_month_calendar(year, month):
    print(f"\n{MONTH_NAMES[month - 1]} {year}:\n")
    print(calendar.month(year, month))


def main():
    today = datetime.date.today()
    year = today.year
    month = today.month

    print("Simple Calendar Viewer")
    print_month_names()
    print_year_calendar(year)

    while True:
        print("Commands:")
        print("  n - next month")
        print("  p - previous month")
        print("  m - show month list")
        print("  a - show whole year calendar")
        print("  y - change year")
        print("  s - select month")
        print("  q - quit")
        choice = input("Enter command: ").strip().lower()

        if choice == "q":
            print("Goodbye.")
            break
        elif choice == "n":
            month += 1
            if month > 12:
                month = 1
                year += 1
            print_month_calendar(year, month)
        elif choice == "p":
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            print_month_calendar(year, month)
        elif choice == "m":
            print_month_names()
        elif choice == "a":
            print_year_calendar(year)
        elif choice == "y":
            year_input = input("Enter year (e.g. 2025): ").strip()
            if year_input.isdigit():
                year = int(year_input)
                print_year_calendar(year)
            else:
                print("Invalid year. Please enter numbers only.")
        elif choice == "s":
            month_input = input("Enter month number (1-12): ").strip()
            if month_input.isdigit():
                month_choice = int(month_input)
                if 1 <= month_choice <= 12:
                    month = month_choice
                    print_month_calendar(year, month)
                else:
                    print("Please enter a number between 1 and 12.")
            else:
                print("Invalid month. Please enter numbers only.")
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
