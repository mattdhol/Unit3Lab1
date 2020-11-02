# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.


num1 = 0
num2 = 1
# num3 = num1 + num2
print ("term: 0 / 50: 0")
print ("term: 1 / 50: 1")
for number in range(2, 51):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print ("term:", number,"/ 50:", num3)


# Hint: The next number is found by adding the two numbers before it
