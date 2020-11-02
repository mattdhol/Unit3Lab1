# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

side_a = int(input("Please Input Side A of triangle"))
side_b = int(input("Please Input Side B of triangle"))
side_c = int(input("Please Input Side C of triangle"))

if side_a == side_b and  side_a == side_c:
    print("This is an equalateral triangle!")
elif side_a != side_b and side_a != side_c and side_b != side_c:
    print(("This is an scalene triangle!"))
else:
    print(("This is an isosceles triangle!"))

    