# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:

phrase = input(" enter a word or phrase ")
while phrase != "leave":
    print(" Your phrase is " + str(len(phrase)) + " characters long ")
    phrase = input(" enter a word or phrase ")
print("Ok, Move On")

#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.