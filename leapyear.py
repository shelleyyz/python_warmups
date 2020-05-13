def is_leap_year(year):

    result = False

    if year % 4 != 0:
        result = False
    elif year % 100 != 0:
        result = True
    elif year % 400 != 0:
        result = False
    else:
        result = True

    print(result)

is_leap_year(2000)
is_leap_year(1997)
is_leap_year(1996)
is_leap_year(1900)
