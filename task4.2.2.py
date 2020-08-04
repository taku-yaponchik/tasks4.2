def is_year_leap(year):
    if year%4==0:
        return "True"
    else:
        return "False"
leap_year=int(input('Enter the year: '))
print(is_year_leap(leap_year))
