from leap_year import IsLeapYear


def test_divide_by_four():
    year = IsLeapYear(1996).divide_by_four()
    assert year == 0


def test_divide_four_hundred():
    year = IsLeapYear(2000).divide_by_four_hundred()
    assert year == 0


def test_divide_hundred():
    year = IsLeapYear(1700).divided_by_hundred()
    assert year == 0


def test_not_divide_by_four():
    year = IsLeapYear(1999).not_divided_by_four()
    assert year != 0


def test_not_divide_hundred():
    year = IsLeapYear(1996).divided_by_hundred()
    assert year != 0


def test_not_divide_four_hundred():
    year = IsLeapYear(1700).not_divide_by_four_hundred()
    assert year != 0


def test_is_leap_year():
    year = IsLeapYear(2000).is_leap_year()
    year_two = IsLeapYear(1996).is_leap_year()
    assert year
    assert year_two


def test_is_not_leap_year():
    year = IsLeapYear(1999).is_leap_year()
    year_two = IsLeapYear(1700).is_leap_year()
    year_three = IsLeapYear(1900).is_leap_year()
    assert not year
    assert not year_two
    assert not year_three

# Hei

