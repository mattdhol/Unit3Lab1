# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
dogs_age = int(input(" Input a dog's age that converts to human years: "))

if dogs_age == 1:
    age = 10
    print(" Your dog's age is " + str(age))
elif dogs_age > 1:
    age = dogs_age * 7 + 6
    print(" Your dog's age is " + str(age))
else:
    print("get a dog")




# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer


   # hum_age = dog_age * 10