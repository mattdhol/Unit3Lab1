# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):

month = input("Enter the month of the year (Jan - Dec)")
day = int(input("Enter the day of the month:"))

if month in ("dec", "jan", "feb", "mar"):
    if (month == "dec" and day >= 21) or (month == "mar" and day <= 19):
        print(day, month, "is in season winter")
    else:
        print(day, month, "is in season winter")
if month in("mar", "apr", "may", "jun"):
    if (month == "mar" and day >= 20) or (month == "jun" and day <=20) or month in("apr", "may"):
        print(day, month, "is in season Spring")
if month in("jun", "aug", "sep", "jul"):
     if (month == "jun" and day >= 21) or (month == "sep" and day <= 21) or month in("aug", "jul"):
        print(day, month, "is in season Summer")
if month in("sep", "oct", "nov", "dec"):
    if (month == "sep" and day >= 22) or (month == "dec" and day <= 20) or month in("oct", "nov"):
        print(day, month, "is in season Fall")


# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.