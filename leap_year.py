class IsLeapYear:
    def __init__(self, year):
        self.year = year

    def divide_by_four(self):
        divide_four = self.year % 4
        if divide_four == 0:
            return divide_four
        else:
            return 1

    def divide_by_four_hundred(self):
        divide_four_hundred = self.year % 400
        if divide_four_hundred == 0:
            return divide_four_hundred
        else:
            return 1

    def divided_by_hundred(self):
        divide_hundred = self.year % 100
        if divide_hundred == 0:
            return divide_hundred
        else:
            return 1

    def not_divide_by_hundred(self):
        not_divide_hundred = self.year % 100
        if not_divide_hundred != 0:
            return not_divide_hundred
        else:
            return 0

    def not_divided_by_four(self):
        not_divide_four = self.year % 4
        if not_divide_four != 0:
            return not_divide_four
        else:
            return 0

    def not_divide_by_four_hundred(self):
        not_divide_four_hundred = self.year % 400
        if not_divide_four_hundred:
            return not_divide_four_hundred
        else:
            return 0

    def is_leap_year(self):
        if IsLeapYear(self.year).divide_by_four_hundred() == 0 or IsLeapYear(self.year).not_divide_by_hundred() != 0\
                and IsLeapYear(self.year).divide_by_four() == 0:
            print(f"{self.year} is a leap year")
            return True
        if IsLeapYear(self.year).not_divide_by_four_hundred() != 0 or IsLeapYear(self.year).divided_by_hundred() == 0\
                and IsLeapYear(self.year).not_divided_by_four() != 0:
            print(f"{self.year} is not a leap year")
            return False


# Check if year is leap year here:
IsLeapYear(2000).is_leap_year()